import psycopg2 ## use this to import table from postgress SQL locally
import pandas as pd
import os
from psycopg2.extras import DictCursor ## to change the row of the table into dictionary
from dotenv import load_dotenv
from psycopg2.extras import execute_values

load_dotenv() ##reads the content from .env file and adds them to the environment 

csv_file_path = os.path.join(os.path.dirname(__file__), 'titanic.csv')
df = pd.read_csv(csv_file_path)

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print('CONNECTION', type(connection)) 

cursor = connection.cursor()
print('CURSOR', type(cursor))

cursor.execute("""DROP TABLE titanic_data""");


cursor.execute("""CREATE TABLE titanic_data(
    Survived integer,
    Pclass integer,
    Name text,
    Sex text,
    Age float,
    SiblingsSpousesAbroad integer,
    ParentsChildrenAbroad integer,
    Fare float
)
""")

execute_values(cursor, """
    INSERT INTO titanic_data
    (Survived, Pclass, Name, Sex, Age, SiblingsSpousesAbroad, ParentsChildrenAbroad, Fare)
    VALUES %s;
""", [tuple(row) for row in df.values])
#query = f"SELECT * FROM {titanic_data};"
#print(query)
#cursor.execute(query) 
#for row in cursor.fetchall():
    #print(row)

query = cursor.execute('''
        SELECT * FROM titanic_data
        ''')
print(query) 
cols = df.columns
print(cols)

result = cursor.fetchone()
print(result)
for row in result:
    print(row)    

connection.commit()

#tuple(row) for row in df.values






   