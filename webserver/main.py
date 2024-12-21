import sqlite3

from flask import Flask, request, Response
from database import DatabaseUtil

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    pass


@app.route("/report-fire", methods=["POST"])
def report_fire():
    db = DatabaseUtil("db.sqlite3")
    try:
        body = request.json()

        db.query("INSERT INTO Fires VALUES (?, FALSE, datetime(), NULL)", body["device-id"])
        db.commit()
    except sqlite3.Error as E:
        print(E)
        return Response(
            status=500
        )
    else:
        return Response(
            status=201
        )
    finally:
        db.close()

@app.route("/suppress-fire", methods=["POST"])
def suppress_fire():
    db = DatabaseUtil("db.sqlite3")
    try:
        body = request.json()

        db.query("UPDATE Fires SET suppressed=1, suppressed_at=datetime() WHERE detector_id=?", body["device-id"])
        db.commit()
    except sqlite3.Error as E:
        print(E)
        return Response(
            status=500
        )
    else:
        return Response(
            status=200
        )
    finally:
        db.close()
