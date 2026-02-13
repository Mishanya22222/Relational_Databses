import sqlite3
import pandas as pd

conn = sqlite3.connect("../baseball.db")
cursor = conn.cursor()

# HAVING is used when we need to filter groups after aggregation you made
# if both columns in the both tables are present, you need to specify which one you want to use by using the table name before the column name, like this: table_name.column_name
# the order of the JOIN matters for the selected columns
query = '''
    SELECT batting.playerID, batting.yearID, teams.name, SUM(batting.HR) AS seasonHR
    FROM batting
    INNER JOIN teams
    ON batting.teamID = teams.teamID AND batting.yearID = teams.yearID
    WHERE batting.playerID = "ruthba01"
    GROUP BY batting.yearID;
'''

cursor.execute(query)
records = cursor.fetchall()
conn.close()

df = pd.DataFrame(records)
print(df)


