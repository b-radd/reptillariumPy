def createMeasurement(conn, measurement):

    sql = """INSERT INTO measurements(measureType,value,timestamp,sensor_id)
    VALUES(?,?,?,?) """

    cur = conn.cursor()
    cur.execute(
        sql,
        (
            measurement.get("measureType"),
            measurement.get("value"),
            measurement.get("timestamp"),
            measurement.get("sensor_id"),
        )
    )
    conn.commit()
    return cur.lastrowid
