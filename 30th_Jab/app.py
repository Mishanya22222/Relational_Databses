# dropdown for all of the PHI matches and when they select this they get to see how many home runs were hit by players with PHI matches
# phillies players ID from 1976

import sqlite3
import gradio as gr
import pandas as pd

def fetch_phillies():
    conn = sqlite3.connect("../baseball.db")
    cursor = conn.cursor()

    query = """
        SELECT playerID
        FROM batting
        WHERE teamID = 'PHI' AND yearID = 1976;
    """

    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    
    # records_df = pd.DataFrame(records, columns=['playerID'])
    phillies_players = []
    for i in records:
        append_value = i[0]
        phillies_players.append(append_value)
    return phillies_players

def f(player):
    conn = sqlite3.connect("../baseball.db")
    cursor = conn.cursor()

    query = """
        SELECT HR
        FROM batting
        WHERE playerID = ? AND yearID = 1976 AND teamID = 'PHI';
    """

    cursor.execute(query, [player])
    records = cursor.fetchall()
    conn.close()
    return records[0][0]

print(f("schmimi01"))  # Example usage to test the function
# iface = gr.Interface(fn=f, inputs = gr.Dropdown(choices = fetch_phillies()), outputs = "number") # choices is a list of options for the dropdown 
# iface.launch()


