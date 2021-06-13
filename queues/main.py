"""
Przetestować działanie algorytmu ze stałymi priorytetami. Przybywające zadania,
czasy ich działania i priorytety dobierać losowo
"""
import queue
import threading
import time
from os import system
from random import randrange, random
import numpy as np

# import matplotlib
# matplotlib.use('TKAgg')
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
#
#

#
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro')
#
# def init():
#     # ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(0, 1)
#     return ln,

# def update(frame):
#     elem = q.get()
#     xdata.append(frame)
#     print(f'Working on {elem}')
#     ydata.append(elem[1](elem[2]))
#     ln.set_data(xdata, ydata)
#     # print(f'Finished {elem}')
#     q.task_done()
#     return ln,
#
#
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
# plt.show()

q = queue.PriorityQueue()


def job(period: int):
    sleep_time = period
    print("Sleeping for: ", sleep_time)
    time.sleep(sleep_time)
    return sleep_time


def worker():
    while True:
        elem = q.get()
        print(f'Working on {elem}')
        elem[1](elem[2])
        # print(f'Finished {elem}')
        q.task_done()


# turn-on the worker thread
threading.Thread(target=worker, daemon=True).start()

i = 0
while i < 200:
    some_val = random()
    q.put((some_val, job, some_val))
    time.sleep(random() * random())
    some_val = random()
    q.put((some_val, job, some_val))
    i += 1
w
print('All task requests sent\n', end='')

# block until all tasks are done
q.join()
print('All work completed')
