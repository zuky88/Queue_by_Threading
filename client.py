#!/usr/bin/env python3

import threading
import datetime
import time
import server

def clientMain():
    i = 0
    while True:
        now = datetime.datetime.now()
        print('[client]send:{0}, {1}'.format(i, now))
        server.msg_send(i)
        i += 1
        time.sleep(0.1)

def thread_start():
    t = threading.Thread(target = clientMain,args=())
    t.setDaemon(True)
    t.start()
