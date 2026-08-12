import time
import threading
import multiprocessing


def heavy():
    total = 0
    for i in range(50_000_000):
        total+=i
    return total

start = time.perf_counter()
heavy()
heavy()
end = time.perf_counter()
print("sequential:", end-start, "secounds")


start = time.perf_counter()
t = threading.Thread(target=heavy)
d = threading.Thread(target=heavy)
t.start()
d.start()
t.join()
d.join()
end = time.perf_counter()
print("Threading:", end-start, "secounds")


start = time.perf_counter()
m = multiprocessing.Process(target=heavy)
q = multiprocessing.Process(target=heavy)

m.start()
q.start()
m.join()
q.join()
end = time.perf_counter()
print("MultiProcessing:", end-start, "secounds")
