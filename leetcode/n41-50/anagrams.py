# -*- coding: utf-8 -*-


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res_dict = {}
        res = []
        for s in strs:
            num = sum(hash(c) for c in s)
            if num not in res_dict:
                res_dict[num] = []
            res_dict[num].append(s)

        for key in res_dict:
            res.append(res_dict[key])

        return res
    
    def groupAnagrams2(self, strs):
        res_dict = {}
        res = []
        for s in strs:
            sord_str = ''.join(sorted(s))
            if sord_str not in res_dict:
                res_dict[sord_str] = []
            res_dict[sord_str].append(s)

        for key in res_dict:
            res.append(res_dict[key])

        return res


print(Solution().groupAnagrams2(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))