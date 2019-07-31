# -*- coding: utf-8 -*-


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))

        index = len(res) - 1
        for i, c2 in enumerate(reversed(num2)):
            for k, c1 in enumerate(reversed(num1)):
                res[index - i - k] += int(c1) * int(c2)
                res[index - i - k - 1] += res[index - i - k] // 10
                res[index - i - k] %= 10

        for i in range(len(res)):
            if not res[i] == 0:
                res = res[i:]
                break
        else:
            res = [0]

        return ''.join([str(x) for x in res])


print(Solution().multiply(num1="123456789", num2="987654321"))
