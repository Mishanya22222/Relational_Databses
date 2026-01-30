import sqlite3
import pandas as pd

conn = sqlite3.connect("../baseball.db") # ../ back up to look in main directory
cursor = conn.cursor()

query = """ 
    SELECT playerID, yearID, teamID, HR
    FROM batting
    WHERE HR >20;
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns=['playerID', 'yearID', 'teamID', 'HR'])
print(records_df)