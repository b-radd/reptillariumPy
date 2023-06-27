import os
from .create_connection import createConnection
from .create_table import createTable


def initialiseDB(db_dir, db_file, relative_path=True, develop=False):

    current_dir = os.getcwd()

    print(current_dir)

    if not os.path.exists(db_dir):
        print("The database directory does not exists. Creating now.")
        if relative_path:
            os.makedirs(
                os.path.join(current_dir, db_dir)
            )
        else:
            os.makedirs(db_dir)

    db_file = os.path.join(current_dir, db_dir, db_file)

    if os.path.isfile(db_file):
        if develop:
            os.remove(db_file)

        else:
            inp = input("The database already exists. Type 'yes' to delete or anything else to escape the database "
                        "initialisation function.")

            if inp.lower() == 'yes':
                os.remove(db_file)
            else:
                exit()

    sql_create_sensors_table = """
        CREATE TABLE IF NOT EXISTS sensors (
            id integer PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sensorType TEXT NOT NULL,
            pin TEXT NOT NULL,
            pinInt integer NOT NULL
        );
        """

    sql_create_measurements_table = """
        CREATE TABLE IF NOT EXISTS measurements (
            id integer PRIMARY KEY AUTOINCREMENT,
            measureType text NOT NULL,
            value REAL,
            timestamp TEXT NOT NULL,
            sensor_id INTEGER NOT NULL,
            vivarium_id INTEGER NOT NULL,
            sensor_position INTEGER NOT NULL,
            FOREIGN KEY (sensor_id) REFERENCES sensors (id)
        );
        """

    # create a database connection
    conn = createConnection(db_file)

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables_all = cursor.fetchall()

    if tables_all:
        # Doping EMPLOYEE table if already exists
        for table in tables_all:
            cursor.execute("DROP TABLE {}".format(table))
            print("Table {} dropped... ".format(table))

            conn.commit()
            conn.close()

    # create tables
    if conn is not None:
        createTable(conn, sql_create_sensors_table)

        createTable(conn, sql_create_measurements_table)
    else:
        print("Error! cannot create the database connection.")
