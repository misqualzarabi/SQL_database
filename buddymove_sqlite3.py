import pandas as pd
buddy = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')

import sqlite3
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
c = conn.cursor()

'''c.execute('CREATE TABLE reviews' (buddy.columns))
conn.commit()'''
buddy.to_sql('reviews', conn, if_exists='replace', index = False)
cursor = conn.cursor()
print("CURSOR", cursor)

"""query = "SELECT * FROM reviews;"
result = cursor.execute(query).fetchall()
print("RESULT ", result)"""

cursor.execute('''
SELECT * FROM reviews
''')
for row in cursor.fetchall():
    print (row)
conn.commit()    