FROM apache/airflow:2.4.0
COPY requirements.txt .
RUN pip install --user --upgrade pip
RUN pip install -r requirements.txt