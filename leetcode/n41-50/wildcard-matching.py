# -*- coding: utf-8 -*-


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        动态规划方法：针对？ * 和普通字符建立一个矩阵，表示其转移
        1 初始0，0位置匹配
        2 如果是Pattern为*，那么当前位置可以匹配到的条件是，只要他的左边 上边 或者左上 任意有一个可以到就可以了
        3 如果是？或相等，那么条件就是左上可以访问到
        4 如果不是，那么久证明不可以访问到了
        """
        pn, sn = len(p), len(s)
        state = {}
        for i in range(pn + 1):
            for k in range(sn + 1):
                state[(i, k)] = False
        state[(0, 0)] = True

        start = 0

        for i in range(1, pn + 1):
            if p[i - 1] == '*':
                state[(i, 0)] = state[(i - 1, 0)]
                for k in range(1, sn + 1):
                    state[(i, k)] = state[(i - 1, k)] or state[(
                        i - 1, k - 1)] or state[(i, k - 1)]
            else:
                start += 1
                for k in range(start, sn + 1):
                    if p[i - 1] == '?' or p[i - 1] == s[k - 1]:
                        state[(i, k)] = state[(i - 1, k - 1)]

        return state[(pn, sn)]

    def isMatch2(self, s, p):
        pn, sn = len(p), len(s)
        i, k = 0, 0
        preP, preS = -1, -1
        while k < sn and i < pn:
            if p[i] == '?' or p[i] == s[k]:
                i, k = i + 1, k + 1
            elif p[i] == '*':
                preP, preS = i, k + 1
                i += 1
            elif preP < 0:
                return False
            else:
                i, k = preP, preS

        while i < pn and p[i] == '*':
            i += 1

        return i == pn and k == sn


print(Solution().isMatch2('aa', '*'))
