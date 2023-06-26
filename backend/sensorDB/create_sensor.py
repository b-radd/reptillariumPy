def createSensor(conn, sensor):

    sql = """INSERT INTO sensors(name,sensorType,pin,pinInt)
    VALUES(?,?,?,?) """

    cur = conn.cursor()
    cur.execute(
        sql,
        (
            sensor.get("name"),
            sensor.get("sensorType"),
            sensor.get("pin"),
            int("".join(filter(str.isdigit, sensor.get("pin")))),
        )
    )
    conn.commit()
    return cur.lastrowid
