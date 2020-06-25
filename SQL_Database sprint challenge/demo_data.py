 
import os
import sqlite3

##DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "chinook.db")

connection = sqlite3.connect('demo_data.sqlite')
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

cursor.execute("""DROP TABLE demo""");
cursor.execute("""CREATE TABLE demo(
    s text,
    x integer,
    y integer
)
""")

cursor.execute("""INSERT INTO demo(s, x, y) VALUES(
    'g',
    '3',
    '9'
),
(
    'v',
    '5',
    '7'
),
(
    'f',
    '8',
    '7'
)
""")
connection.commit()

cursor.execute('''
        SELECT * FROM demo
        ''')


result = cursor.fetchall()
print (len(result))  

cursor.execute('''
    SELECT * FROM demo
    WHERE x AND y = 5
    ''')
results = cursor.fetchall()
print (len(results))

cursor.execute('''
    SELECT count(DISTINCT y) FROM demo
    ''')
RESULT = cursor.fetchall() 
print(RESULT)  











