# -*- coding: utf-8 -*-

from collections import deque
import heapq
import numpy as np


def deque_test():
    '''
    队列测试，可用于普通队列、栈、双端队列
    '''
    arr = [x**2 for x in range(1, 20)]

    print(arr)

    q = deque(maxlen=5)

    for x in arr:
        q.append(x)

    print(q.pop())
    print(q)

    q.appendleft(1000)
    print(q)

    print(q.popleft())
    print(q)


def heapq_test():
    '''
    堆测试，可用于自动堆排序，获取最大最小元素
    '''
    narr = np.random.rand(20)
    top5Max = heapq.nlargest(5, narr)
    print(top5Max)

    top5Min = heapq.nsmallest(5, narr)
    print(top5Min)

    lst_heap = list(narr)
    heapq.heapify(lst_heap)
    print(lst_heap)
    print(heapq.heappop(lst_heap))
    print(heapq.heappop(lst_heap))
    print(heapq.heappop(lst_heap))
    print(heapq.heappop(lst_heap))

    portfolio = [{
        'name': 'IBM', 'shares': 100, 'price': 91.1 }, {
        'name': 'AAPL', 'shares': 50, 'price': 543.22 }, {
        'name': 'FB', 'shares': 200, 'price': 21.09 }, {
        'name': 'HPQ', 'shares': 35, 'price': 31.75 }, {
        'name': 'YHOO', 'shares': 45, 'price': 16.35 }, {
        'name': 'ACME', 'shares': 75, 'price': 115.65
    }]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    print(cheap)






heapq_test()
