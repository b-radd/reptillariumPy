def createMeasurement(conn, measurement):

    sql = """INSERT INTO measurements(measureType,value,timestamp,sensor_id,vivarium_id,sensor_position)
    VALUES(?,?,?,?,?,?) """

    cur = conn.cursor()
    cur.execute(
        sql,
        (
            measurement.get("measureType"),
            measurement.get("value"),
            measurement.get("timestamp"),
            measurement.get("sensor_id"),
            measurement.get("vivarium_id"),
            measurement.get("sensor_position"),
        )
    )
    conn.commit()
    return cur.lastrowid
