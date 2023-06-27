import os
import serial
from backend.sensorRead import sensorReader
from backend.sensorDB import initialiseDB

first_time = False
develop = False
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


# def translate_measurement_type(value):
#     if value == 'T':
#         return 'temperature'
#     elif value == 'H':
#         return 'humidity'
#     elif value == 'UV':
#         return 'uv'
#     else:
#         raise TypeError
#
#
# ser = serial.Serial('/dev/ttyACM0')
#
#
# while True:
#     s = ser.readline().decode()
#     if s != '':
#         # now = datetime.now()
#         # current_time = now.strftime("%Y-%m-%d %H:%M:%S")
#
#         rows = [x.split(':') for x in s.split(',')]
#         rows = [y.strip() for x in rows for y in x]
#
#         tmp_sensor_id = rows[::2]
#         tmp_sensor_value = rows[1::2]
#
#         for i, sensorID in enumerate(tmp_sensor_id):
#             measurement_type, sensor_pos = sensorID.split('_')
#             vivarium_no, sensor_location = sensor_pos.split('.')
#
#             value = tmp_sensor_value[i]
#
#             measurement_type = translate_measurement_type(measurement_type)
#
#             print(vivarium_no, sensor_location, measurement_type, value)



