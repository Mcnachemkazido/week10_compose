import os
from dotenv import load_dotenv
import pymysql


class Connection:
    def __init__(self):
        load_dotenv()
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.database=os.getenv("DB_DATABASE")

    def get_connection(self):
        try:
            return pymysql.connect(user=self.user,password=self.password,
                                   host=self.host,database=self.database)
        except Exception as e:
            print(e)


