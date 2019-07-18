# -*- coding: utf-8 -*-
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        if not strs:
            return ''

        min_len = min([len(s) for s in strs])

        for i in range(min_len):
            c = strs[0][i]
            for k in range(1, len(strs)):
                if c != strs[k][i]:
                    return res
            res = res + c

        return res


print(Solution().longestCommonPrefix(['aca','cba']))
