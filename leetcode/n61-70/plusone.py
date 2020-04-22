# -*- coding:utf-8 -*-
class Solution:
    def plusOne(self, digits):
        num = 0
        for i in digits:
            num = num * 10 + i
        num = num + 1
        return [int(i) for i in str(num)]

print(Solution().plusOne([2, 3, 4]))
