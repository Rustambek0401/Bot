import psycopg2 as db
import os

class DataBasa:
    @staticmethod
    def postgrestt(quer,type):
        dataBase = db.connect(
            database= "n37",
            user="postgres",
            host="localhost",
            password= "rus19tam98"
        )
        cursor = db.cursor()
        cursor.execute(quer)
        if type == 'insert':
            dataBase.commit()
            return "insert"
        else:
            return cursor.fetchall()