from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from  sqlalchemy.sql.expression import func, select

class Persistence:
    def __init__(self):
        self.engine = create_engine('postgresql://airflow:airflow@localhost:5433/airflow', echo = True)
        self.connection = self.engine.connect()

    def select_data(self,category):
        """
        Select news from a database
        Args:
            category: Category of the news
        Return:
            row: Tuple of uuid and headline
        """
        query = "SELECT uuid,headline FROM amharicnews "
        query += "where category={} ORDER BY random() limit(1)".format(category)
        t = text(query)
        result = self.connection.execute(t)
        row = ''
        for i in result:
            row = i 
        return row
