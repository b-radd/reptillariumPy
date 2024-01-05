import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

now = datetime.now()
backdate = now - timedelta(days=3)

# Read sqlite query results into a pandas DataFrame
conn = sqlite3.connect("./db/sensorData.sqlite")
df = pd.read_sql_query(
    """
    SELECT * FROM measurements WHERE measureType='humidity' AND timestamp>= datetime('now','-2 day')
    """,
    con=conn)

# Verify that result of SQL query is stored in the dataframe
# print(df.to_string())

conn.close()

print(df.to_string())

# for group, data in df.groupby('vivarium_id'):
#     print(group)
#     data[['timestamp', 'value']].plot()
#
# plt.show()
