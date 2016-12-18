import json
import sys
import os

while(True):
    try:
        while(True):
            inpath = "/tmp/inpFifo"
            try:
                os.mkfifo(inpath)
            except:
                print "file is exsist"

            print "Wait for fifo read"
            fifoin = open(inpath, 'r')
            msg = fifoin.read()
            fifoin.close()
            data = json.loads(msg)
            print data

    except Exception, e:
        print e