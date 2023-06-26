import sqlite3


def get_sensor_by_id(sqlite_db, sensor_id):
    conn = sqlite3.connect(sqlite_db)
    curs = conn.cursor()
    # for row in curs.execute("SELECT * FROM measurements ORDER BY timestamp DESC LIMIT 1"):
    for row in curs.execute(
            "SELECT * "
            "FROM sensors "
            "WHERE id={} "
            "".format(sensor_id)
    ):
        sid, name, sensorType, pin, pinInt = row

    conn.close()

    return sid, name, sensorType, pin, pinInt


def get_sensor_id_by_pin(sqlite_db, pin):
    conn = sqlite3.connect(sqlite_db)
    curs = conn.cursor()
    # for row in curs.execute("SELECT * FROM measurements ORDER BY timestamp DESC LIMIT 1"):
    for row in curs.execute(
            "SELECT * "
            "FROM sensors "
            "WHERE pin='{}' "
            "".format(pin)
    ):
        sid, name, sensorType, pin, pinInt = row

    conn.close()

    return sid


def get_latestData_by_sensorID(sqlite_db, sensor_id):
    conn = sqlite3.connect(sqlite_db)
    curs = conn.cursor()
    # for row in curs.execute("SELECT * FROM measurements ORDER BY timestamp DESC LIMIT 1"):
    row = curs.execute(
        "SELECT COUNT( DISTINCT measureType) as measurementTypes "
        "FROM measurements "
        "WHERE sensor_id={} "
        "".format(sensor_id)
    )

    measurementTypes = list(sum(row.fetchall(), ()))[0]

    dict_return = {}

    if measurementTypes == 1:

        for row in curs.execute(
                "SELECT measureType, value, timestamp, sensor_id "
                "FROM measurements "
                "WHERE sensor_id={} "
                "ORDER BY timestamp DESC LIMIT 1"
                "".format(sensor_id)
        ):
            measurement, value, timestamp, sensor_id = row

        dict_return = {
            "sensor_id": sensor_id,
            "measurementType": {
                measurement: {
                    "measurementValue": value,
                    "timeStamp": timestamp,
                }
            }
        }

    elif measurementTypes > 1:

        dict_return = {
            "sensor_id": sensor_id,
            "measurementType": {}
        }

        measurements = []

        for row in curs.execute(
                "SELECT DISTINCT measureType "
                "FROM measurements "
                "WHERE sensor_id={} "
                "".format(sensor_id)
        ):
            measurements.append(row[0])

        for measure in measurements:

            for row in curs.execute(
                    "SELECT measureType, value, timestamp, sensor_id "
                    "FROM measurements "
                    "WHERE sensor_id={} "
                    "AND measureType='{}' "
                    "ORDER BY timestamp DESC LIMIT 1"
                    "".format(sensor_id, measure)
            ):
                measurement, value, timestamp, sensor_id = row

                dict_return["measurementType"][measurement] = {
                    "measurementValue": value,
                    "timeStamp": timestamp,
                }

    conn.close()

    return dict_return

