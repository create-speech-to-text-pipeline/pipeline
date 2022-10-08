from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
# from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from airflow.models import Variable
from airflow.utils.dates import days_ago
from scripts.dataloader import DataLoader
from scripts.db_connection import Connection

import pandas as pd


default_args = {
    'owner': 'wangui',
    'depends_on_past': False,
    'retries': 1,
    'start_date': datetime(2022, 10, 8),
    'retry_delay': timedelta(minutes=5)
}


def read_data():
    """csv data reading only
    """
    dl = DataLoader()
    df = dl.read_csv('/opt/airflow/data/AmharicNewsDataset.csv')
    df.to_csv('./readAmharic.csv',index=False)

def create_table():
    """create postgresql table"""
    con = Connection()
    con.create_table()

def data_to_db():
    """Insert data to db"""
    con = Connection()
    news = pd.read_csv('./mnt/10ac-batch-6/bucket/transformed_db.csv')
    con.df_to_sql('amharicnews', news)

with DAG(
    dag_id='input_transform_output',
    default_args=default_args,
    description='receive data from kafka, send it to spark for transformation, output spark data to s3 bucket',
    schedule_interval='@once',
    catchup=False,
    dagrun_timeout=timedelta(minutes=60),
    tags=['spark']
) as dag:
    get_bytes_from_kafka = PythonOperator(
        task_id='read_data',
        python_callable=read_data,
        dag=dag,
    )
    run_spark_transformation = BashOperator(
        task_id='spark_tranformation',
        # **change this to proper path on aws server
        bash_command='bash /home/akr/Desktop/pipeline/airflow/scripts/spark_transformation.sh ', 
        dag=dag,
    )
    create_a_table = PythonOperator(
        task_id="table_creator",
        python_callable=create_table
    )
    data_to_bucket = PythonOperator(
        task_id='data_to_bucket',
        python_callable=data_to_db,
        dag=dag,
    )

get_bytes_from_kafka >> run_spark_transformation >> create_a_table >> data_to_bucket
get_bytes_from_kafka >> create_a_table >> data_to_bucket

