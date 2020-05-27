import psycopg2 ## use this to import table from postgress SQL locally
import pandas as pd
import os
from psycopg2.extras import DictCursor ## to change the row of the table into dictionary
from dotenv import load_dotenv

load_dotenv() ##reads the content from .env file and adds them to the environment 


DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print('CONNECTION', type(connection))                        
### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor(cursor_factory=DictCursor)
  
 




### An example query
cursor.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cursor.fetchall()
for row in result:
    cols = list(row.keys()) ###get name of columns of a table
    print(cols)
    print("_____")
    print(type(row))
    print(row) ### print all the rows
    ## print(row["name"]), get the row of one column

