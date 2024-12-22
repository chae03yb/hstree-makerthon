def resolve_dependencies():
    import os

    os.system("python -m pip install -r webserver/requirements.txt")


def setup_database():
    import sqlite3

    connection = sqlite3.connect("webserver/db.sqlite3")
    try:
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE Devices (
            device_id        INT AUTO_INCREMENT,
            device_latitude  REAL NOT NULL,
            device_longitude REAL NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE Fires (
            detector_id   INT,
            suppressed    BOOL     DEFAULT FALSE,
            started_at    DATETIME NOT     NULL,
            suppressed_at DATETIME
        );
        """)

        connection.commit()
    except sqlite3.Error:
        print("Failed to initialize DB")
    else:
        print("Successfully initialized DB")
    finally:
        connection.close()


def setup():
    print("Setting up webserver...")
    resolve_dependencies()
    setup_database()