import json

def filter(data):
    alert = {}
    alert["To"] = 3
    alert["lat"] = data["lat"]
    alert["lon"] = data["lon"]
    alert["sname"] = data["sname"]

