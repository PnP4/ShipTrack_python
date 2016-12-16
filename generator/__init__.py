import random
import time
import json


def genarate():
    lat = random.uniform(6.9218386, 7.2418386)
    lon = random.uniform(79.8562055, 80.5062055)
    sname = "Ship" + str(random.random())
    alert = {}
    alert["lat"] = lat
    alert["lon"] = lon
    alert["sname"] = sname
    alert["time"] = time.time()
    alert["shiptype"] = "Navy"
    return alert