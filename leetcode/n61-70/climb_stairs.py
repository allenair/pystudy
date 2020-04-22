# -*- coding:utf-8 -*-
class Solution:
    num_map = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if self.num_map.get(n - 1) != None:
                path_one = self.num_map[n - 1]
            else:
                path_one = self.climbStairs(n - 1)
                self.num_map[n - 1] = path_one
            if self.num_map.get(n - 2) != None:
                path_two = self.num_map[n - 2]
            else:
                path_two = self.climbStairs(n - 2)
                self.num_map[n - 2] = path_two
            return path_one + path_two


print(Solution().climbStairs(38))