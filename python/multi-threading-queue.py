import time
import threading
import os
import queue
import random

class Worker(threading.Thread):
  def __init__(self, queue, num):
    threading.Thread.__init__(self)
    self.queue = queue
    self.num = num
    print("Enabled worker {}".format(self.num))

  def run(self):
    while self.queue.qsize() > 0:
      # Get data from queue
      task = self.queue.get()

      # For monitoring CPUs (Comment out if not needed)
      # for i in range(6000000): t = i + 1

      # For monitoring I/O
      time.sleep(random.uniform(0.1, 5))

      print("Worker %d: %s" % (self.num, task))
      

# Config
workerNum = os.cpu_count();
print("Number of workers (CPU cores) to start multithreading: {}".format(workerNum))

queue = queue.Queue()

# Put tasks into the queue
for i in range(100):
  queue.put("Data %d" % i)

worker = {}
for i in range(workerNum):
    worker[i] = Worker(queue, i)
    worker[i].start()

# Wait for all workers to complete
for i in worker:
    worker[i].join()

print("Done.")