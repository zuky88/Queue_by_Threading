#!/usr/bin/env python3

import threading
import queue
import datetime

gq = queue.Queue()


def thread_start():
    global gq
    t = threading.Thread(target = serverMain, args = (gq,))
    t.setDaemon(True)
    t.start()


def serverMain(q:queue.Queue):
    while True:
        msg = q.get()
        now = datetime.datetime.now()
        print('[server]get:{0}, {1}'.format(msg, now))
        q.task_done()

def msg_send(msg):
    global gq
    gq.put(msg)

