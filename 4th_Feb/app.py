import sqlite3
import pandas as pd

conn = sqlite3.connect("../baseball.db")
cursor = conn.cursor()

# query = '''
    # SELECT playerID, SUM(HR) AS careerHR
    # FROM batting
    #GROUP BY playerID
    #ORDER BY careerHR DESC
    #LIMIT 10;
#'''

query = '''
    SELECT yearID, SUM(HR) as totalHR
    FROM batting
    WHERE teamID = "PHI"
    GROUP BY yearID
    ORDER BY yearID DESC;
'''
cursor.execute(query)
records = cursor.fetchall()
conn.close()

df = pd.DataFrame(records, columns=['yearID', 'totalHR'])
print(df)