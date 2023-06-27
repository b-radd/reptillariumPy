import pandas as pd
import sqlite3

# Read sqlite query results into a pandas DataFrame
conn = sqlite3.connect("./db/sensorData.sqlite")
df = pd.read_sql_query(
    """
    SELECT * FROM measurements WHERE measureType='temperature' AND vivarium_id=1
    """,
    conn)

# Verify that result of SQL query is stored in the dataframe
print(df.to_string())

conn.close()
