# -*- coding: utf-8 -*-
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        num_map = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ''
        }

        res = ['']

        for i in range(len(digits)):
            res = [m + n for m in res for n in list(num_map[digits[i]])]

        return res


print(Solution().letterCombinations("23"))