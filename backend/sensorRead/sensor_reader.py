import sys
import time
import serial
from datetime import datetime

from ..sensorDB.create_connection import createConnection
from ..sensorDB.create_measurement import createMeasurement
from ..sensorDB.create_sensor import createSensor
from ..sensorDB.sensor_list import sensorList
from ..sensorDB.retrieve import get_sensor_by_id


def translate_measurement_type(value):
    if value == 'T':
        return 'temperature'
    elif value == 'H':
        return 'humidity'
    elif value == 'UV':
        return 'uv'
    else:
        raise TypeError


def sensorReader(database, delay=60*5):

    ser = serial.Serial('/dev/ttyACM0')

    # conn = createConnection(database)
    #
    # sensor_id = {}
    #
    # sensors = sensorList()
    #
    # for sensorKey, sensorData in sensors.items():
    #     sensor_id[sensorKey] = {
    #         'id': createSensor(conn, sensorData)
    #     }
    #
    # conn.close()

    while True:

        try:
            s = ser.readline().decode()

            if s != '':
                now = datetime.now()
                current_time = now.strftime("%Y-%m-%d %H:%M:%S")

                rows = [x.split(':') for x in s.split(',')]
                rows = [y.strip() for x in rows for y in x]

                tmp_sensor_id = rows[::2]
                tmp_sensor_value = rows[1::2]

                for i, sensorID in enumerate(tmp_sensor_id):
                    measurement_type, sensor_pos = sensorID.split('_')
                    vivarium_no, sensor_location = sensor_pos.split('.')

                    value = tmp_sensor_value[i]

                    measurement_type = translate_measurement_type(measurement_type)

                    # print(vivarium_no, sensor_location, measurement_type, value)

                    conn = createConnection(database)

                    createMeasurement(
                            conn,
                            {
                                "measureType": measurement_type,
                                "value": value,
                                "timestamp": current_time,
                                "sensor_id": sensorID,
                                'vivarium_id': vivarium_no,
                                'sensor_position': sensor_location,
                            }
                        )

                    conn.close()

        except KeyboardInterrupt:
            sys.exit(0)

