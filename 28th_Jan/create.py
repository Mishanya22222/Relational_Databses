# cd .. is for going back to the parent directory
# import sqlite3 and pandas

import sqlite3
import pandas as pd

# Create a new SQLite database (or connect to an existing one)
conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()

# Read data from a CSV file and store it in the df variable
df = pd.read_csv('../people.csv')
# Write the DataFrame to a SQL table named 'batting'
# batting is the name of the table
df.to_sql('people', conn, if_exists='replace', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()