import time

from ..sensorDB.create_connection import createConnection
from ..sensorDB.create_measurement import createMeasurement
from ..sensorDB.create_sensor import createSensor
from ..sensorDB.sensor_list import sensorList
from ..sensorDB.retrieve import get_sensor_by_id


def sensorReader(database, delay=60*5):

    conn = createConnection(database)

    sensor_id = {}

    sensors = sensorList()

    for sensorKey, sensorData in sensors.items():
        sensor_id[sensorKey] = {
            'id': createSensor(conn, sensorData)
        }

    conn.close()



    # for sid in sensor_id:
    #     if "uv" in sid:
    #         si, sname, sdesc, spin, spin_int = get_sensor_by_id(database, sensor_id.get(sid).get("id"))
    #         sensor_id[sid]["pin"] = spin_int
    #         sensor_id[sid]["instance"] = UVSensor(board, spin_int, differential=0)
    #     elif "dht" in sid:
    #         si, sname, sdesc, spin, spin_int = get_sensor_by_id(database, sensor_id.get(sid).get("id"))
    #         sensor_id[sid]["pin"] = spin_int
    #         sensor_id[sid]["instance"] = DHTSensor(board, spin_int, 22)
    #     elif "ow" in sid:
    #         si, sname, sdesc, spin, spin_int = get_sensor_by_id(database, sensor_id.get(sid).get("id"))
    #         sensor_id[sid]["pin"] = spin_int
    #         sensor_id[sid]["instance"] = None
    #
    # while True:
    #     try:
    #         for sid in sensor_id:
    #             if "uv" in sid:
    #
    #                 uv = sensor_id.get(sid).get("instance")
    #
    #                 if uv.data:
    #
    #                     conn = create_connection(database)
    #                     create_measurement(
    #                             conn,
    #                             {
    #                                 "measureType": "uv index",
    #                                 "value": uv.data.get("measurements").get("uv index"),
    #                                 "timestamp": uv.data.get("timestamp"),
    #                                 "sensor_id": sensor_id.get(sid).get("id"),
    #                             }
    #                         )
    #
    #                     conn.close()
    #
    #             elif "dht" in sid:
    #
    #                 dht = sensor_id.get(sid).get("instance")
    #
    #                 if dht.data:
    #
    #                     conn = create_connection(database)
    #                     create_measurement(
    #                         conn,
    #                         {
    #                             "measureType": "temperature",
    #                             "value": dht.data.get("measurements").get("temperature"),
    #                             "timestamp": dht.data.get("timestamp"),
    #                             "sensor_id": sensor_id.get(sid).get("id"),
    #                         }
    #                     )
    #                     create_measurement(
    #                         conn,
    #                         {
    #                             "measureType": "humidity",
    #                             "value": dht.data.get("measurements").get("humidity"),
    #                             "timestamp": dht.data.get("timestamp"),
    #                             "sensor_id": sensor_id.get(sid).get("id"),
    #                         }
    #                     )
    #
    #                     conn.close()
    #
    #             elif "ow" in sid:
    #
    #                 ow = OneWireSensor(board, sensor_id.get(sid).get("pin"))
    #
    #                 conn = create_connection(database)
    #
    #                 create_measurement(
    #                     conn,
    #                     {
    #                         "measureType": "temperature",
    #                         "value": ow.data.get("measurements").get("temperature"),
    #                         "timestamp": ow.data.get("timestamp"),
    #                         "sensor_id": sensor_id.get(sid).get("id"),
    #                     }
    #                 )
    #
    #                 conn.close()
    #
    #         time.sleep(read_time)
    #
    #     except KeyboardInterrupt:
    #         board.shutdown()
    #         sys.exit(0)


