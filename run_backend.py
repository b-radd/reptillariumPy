import os
from backend.sensorRead import sensorReader
from backend.sensorDB import initialiseDB

first_time = True
develop = True
sqlite_db_dir = './db'
sqlite_db_file = 'sensorData.sqlite'

if first_time:
    initialiseDB(sqlite_db_dir, sqlite_db_file, develop=develop)
    sensorReader(
        os.path.join(
            sqlite_db_dir, sqlite_db_file
        ),
    )
elif develop:
    sensorReader(
        os.path.join(
            sqlite_db_dir, sqlite_db_file
        ),
        delay=10.
    )
else:
    sensorReader(
        os.path.join(
            sqlite_db_dir, sqlite_db_file
        ),
    )

