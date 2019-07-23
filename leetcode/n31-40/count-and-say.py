# -*- coding: utf-8 -*-


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(2, n + 1):
            tmp = []
            count, last = 0, None
            for c in range(len(res)):
                if not last or res[c] == last:
                    count += 1
                else:
                    tmp.append(str(count))
                    tmp.append(last)
                    count = 1
                last = res[c]
            else:
                tmp.append(str(count))
                tmp.append(res[c])
            res = ''.join(tmp)

        return res


print(Solution().countAndSay(6))
