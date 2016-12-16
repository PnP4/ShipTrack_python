import json
import __init__

while(True):
    try:
      while(True):
          alert = __init__.genarate()
          message=json.dumps(alert)
          print message
          # should send the message
    except Exception, e:
        print e