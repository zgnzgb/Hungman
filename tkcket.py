import time
import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqu(self,item):
        self.items.insert(0,item)

    def dequ(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def sim_line(self,till_show,max_time):
        pq = Queue()
        tix_sold = []

        for i in range(10):
            pq.enqu("person" + str(i))

        t_end = time.time() + till_show
        now = time.time()

        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0,max_time)
            time.sleep(r)
            person = pq.dequ()
            print(person)
            tix_sold.append(person)

        return tix_sold

queue = Queue()
sold = queue.sim_line(5,1)
print(sold)