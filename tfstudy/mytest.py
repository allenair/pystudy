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

# myredis = redis.Redis(host='192.168.1.147', port=6379, db=0)
# with open('D:\\code\\sts-project\\py_study\\library\\vec_all_200_hs.txt', 'r', encoding='utf-8') as fin:
#     for line in fin.readlines():
#         lst = line.split()
#         if len(lst) > 3:
#             # arr = [float(lst[i]) for i in range(1,len(lst))]
#             myredis.rpush(lst[0],*lst[1:])

# mydict = {}
# mydict['A'] = 0.9876
# mydict['b'] = 0.8876
# mydict['c'] = 0.9976
# mydict['d'] = 0.5876
# mydict['e'] = 0.6876
# sorted_res = sorted(mydict.items(), key=lambda item: item[1], reverse=True)
# print(sorted_res)

# def test():
#     mydict['z']=345
#     print(mydict)
# test()
# print(mydict)

# with open('d:/test.txt','a',encoding='utf-8') as fout:
#     for i in range(len(sorted_res)):
#         fout.write('{}>>{:1.4f}\n'.format(sorted_res[i][0],sorted_res[i][1]))
#     lst = [2,3,4,5,6]
#     fout.write(','.join(lst))


def deal_csv_file(inputFileName, outputFileName):
    lst = []
    str = ''
    with open(inputFileName, 'r', encoding='utf-8') as fin:
        for line in fin.readlines():
            line = line.strip()
            if len(line) > 0 and line[0] == '"' and len(str) > 0:
                lst.append(str)
                str = line
                # print('='*30 + str[:20])
            else:
                str = str + ' ' + line

    if len(str) > 0:
        lst.append(str)

    with open(outputFileName, 'w', encoding='utf-8') as fout:
        for line in lst:
            if len(line) > 5:
                line = line[1:]
                if line[-1] == '"':
                    line = line[:-1]
                fout.write(line + '\n')


# deal_csv_file('d:/new_all_data.csv', 'd:/all_data_result.txt')

with open('d:/result2.txt','r',encoding='utf-8') as fin:
    for index, line in enumerate(fin.readlines()):
        print('{:3d} >>> {}'.format(index+1, line))