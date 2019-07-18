# -*- coding: utf-8 -*-
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        for i in range(len(s) - 1):
            if map_dict[s[i]] < map_dict[s[i + 1]]:
                res = res - map_dict[s[i]]
            else:
                res = res + map_dict[s[i]]
        res = res + map_dict[s[-1]]

        return res


print(Solution().romanToInt('MCMXCIV'))