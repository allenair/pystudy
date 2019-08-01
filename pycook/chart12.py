# -*- coding: utf-8 -*-

import time
from threading import Thread
import multiprocessing
import os


def task(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


def thread_test():
    t = Thread(target=task, args=(5, ))
    t.start()

    for i in range(30):
        print('=' * 20)
        time.sleep(1)


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(2)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    # thread_test()
    # processor_test()

    # print('Parent process %s.' % os.getpid())
    # p = multiprocessing.Process(target=run_proc, args=('test',))
    # print('Child process will start.')
    # p.start()
    # p.join()
    # print('Child process end.')

    print('Parent process %s.' % os.getpid())
    p = multiprocessing.Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i, ))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')