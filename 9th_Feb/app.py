import sqlite3
import pandas as pd

conn = sqlite3.connect("../baseball.db")
cursor = conn.cursor()

# HAVING is used when we need to filter groups after aggregation you made
query = '''
    SELECT teamID, SUM(HR) AS seasonHR
    FROM batting
    WHERE yearID = 2025
    GROUP BY teamID HAVING seasonHR > 200
    ORDER BY seasonHR DESC;
'''

cursor.execute(query)
records = cursor.fetchall()
conn.close()

df = pd.DataFrame(records, columns = ['teamID', 'seasonHR'])
print(df)


