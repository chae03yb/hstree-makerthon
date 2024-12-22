import requests


def send_alarm(device_id: int):
    requests.post(
        "http://localhost:8720/report-fire",
        json={
            "device-id": device_id
        },
    )


def suppress_alarm(device_id: int):
    requests.post(
        "http://localhost:8720/suppress-fire",
        json={
            "device-id": device_id
        },
    )
