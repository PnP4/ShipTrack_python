import __init__
#data=json.loads('{"lat": 7.217592304415584, "sname": "Ship0.284266547671", "lon": 80.08063450635785, "shiptype": "Navy", "time": 1474300567.82514}')



while(True):
    try:
        while(True):
            __init__.channel.basic_consume(__init__.callback,
                      queue='datafilter',
                      no_ack=True)

            __init__.channel.start_consuming()

    except Exception, e:
        print e
