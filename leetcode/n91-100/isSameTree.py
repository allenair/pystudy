# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        if p == None and q != None or p != None and q == None:
            return False
        if p.val == q.val:
            lflag = self.isSameTree(p.left, q.left)
            if not lflag:
                return False
            return self.isSameTree(p.right, q.right)

        else:
            return False


r1 = TreeNode(1)
a1 = TreeNode(2)
r1.left = a1

r2 = TreeNode(1)
a2 = None
b2 = TreeNode(2)
r2.left = a2
r2.right = b2

print(Solution().isSameTree(r1, r2))
