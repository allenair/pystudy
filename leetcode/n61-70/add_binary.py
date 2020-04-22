# -*- coding:utf-8 -*-
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ia = int(a, base=2)
        ib = int(b, base=2)
        return str(bin(ia + ib))[2:]


print(Solution().addBinary("11", "1"))
