import pyttsx
import time
from Queue import Queue
from threading import Thread

q = Queue()

def say_loop():
    engine = pyttsx.init()
    while True:
        engine.say(q.get())
        engine.runAndWait()
        q.task_done()

def first_iteration():
    t = Thread(target=say_loop)
    t.daemon = True
    t.start()
    for i in range(0, 3):
        q.put(' ')

def continous(str):
    q.put(str)

if __name__=="__main__":

    while True:
        first_iteration()
        time.sleep(2)
        str = 'Something Something Something'
        continous(str)
        

