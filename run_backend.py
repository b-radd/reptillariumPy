import os
import serial
from backend.sensorRead import sensorReader
from backend.sensorDB import initialiseDB

first_time = True
develop = True
sqlite_db_dir = './db'
sqlite_db_file = 'sensorData.sqlite'

# if first_time:
#     initialiseDB(sqlite_db_dir, sqlite_db_file, develop=develop)
#     sensorReader(
#         os.path.join(
#             sqlite_db_dir, sqlite_db_file
#         ),
#     )
# elif develop:
#     sensorReader(
#         os.path.join(
#             sqlite_db_dir, sqlite_db_file
#         ),
#         delay=10.
#     )
# else:
#     sensorReader(
#         os.path.join(
#             sqlite_db_dir, sqlite_db_file
#         ),
#     )

ser = serial.Serial('/dev/ttyACM0')

while True:
    s = ser.readline().decode()
    if s != '':
        # now = datetime.now()
        # current_time = now.strftime("%Y-%m-%d %H:%M:%S")

        rows = [x.split(':') for x in s.split(',')]
        # rows = [y.strip() for x in rows for y in x]

        print(rows)

