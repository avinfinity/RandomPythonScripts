import threading
import time

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

class NewThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      threadLock.acquire()
      print_time(self.name, 3, self.counter)
      threadLock.release()


threadLock = threading.Lock()
threads = []
thread1 = NewThread(1, "NewThread-1", 1)
thread2 = NewThread(2, "NewThread-2", 2)
thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

print("Exiting Main Thread")
