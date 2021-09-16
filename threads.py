from threading import *
from time import sleep
class Nanda(Thread):
    def run(self):
        for i in range(8):
            print("Nanda")
            sleep(1)

class Kumar(Thread):
    def run(self):
        for i in range(8):
            print("Kumar")
            sleep(1)

nan = Nanda()
kum = Kumar()
nan.start()
sleep(0.2)
kum.start()
nan.join()
kum.join()
print("termination of main thread")