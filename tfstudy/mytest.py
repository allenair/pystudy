import math
import mydemo
import redis

# sv1 = [1, 1, 2, 1, 1, 1, 0, 0, 0]
# sv2 = [1, 1, 1, 0, 1, 1, 1, 1, 1]

# dotVal = sum([sv1[i] * sv2[i] for i in range(len(sv1))])
# rank1 = math.sqrt(sum([sv1[i]**2 for i in range(len(sv1))]))
# rank2 = math.sqrt(sum([sv2[i]**2 for i in range(len(sv2))]))

# print(dotVal / (rank1 * rank2))

# word_dict = {'a': [0.1, 0.2, 0.3], 'b': [0.5, 0.7, 0.1], 'c': [0.2, 0.4, 0.6]}
# res = []
# for _, vector in word_dict.items():
#     if not res:
#         res = [0.0] * len(vector)
#     res = [res[i] + vector[i] for i in range(len(res))]

# print(res)
# tmp = [res[i]**2 for i in range(len(res))]
# total = sum(tmp)
# total = math.sqrt(total)
# print([res[i] / total for i in range(len(res))])

myredis = redis.Redis(host='192.168.1.147', port=6379, db=0)

with open('D:\\code\\sts-project\\py_study\\library\\vec_all_200_hs.txt', 'r', encoding='utf-8') as fin:
    for line in fin.readlines():
        lst = line.split()
        if len(lst) > 3:
            # arr = [float(lst[i]) for i in range(1,len(lst))]
            myredis.rpush(lst[0],*lst[1:])

