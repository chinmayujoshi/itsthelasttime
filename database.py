from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()
engine = create_engine("mysql+pymysql://sql12665856:Wpn7kYU1r8@sql12.freemysqlhosting.net/sql12665856")


def addScore(timestamp, score):
    query = text("INSERT INTO log (timestamp, score) VALUES (:timestamp, :score)")
    params = {'timestamp': timestamp, 'score': score}

    try:
        print("Executing SQL Query:")
        print(query)
        print("Parameters:")
        print(params)

        with engine.connect() as conn:
            result = conn.execute(query.bindparams(**params))
            conn.commit() 

        print("Insert successful.")
        return result

    except Exception as e:
        print("Error during insertion:")
        print(str(e))
        raise  # Re-raise the exception after logging it

def its_a_date(selected_value):
    query = text("INSERT INTO date (date) VALUES (:date)")
    params = {'date': selected_value}
    with engine.connect() as conn:
            result = conn.execute(query.bindparams(**params))
            conn.commit() 
