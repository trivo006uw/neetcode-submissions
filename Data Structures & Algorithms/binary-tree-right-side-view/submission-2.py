# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        q = collections.deque()
        q.append(root)

        res = []

        while q:
            level = [] 
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.right:
                    if node.right is None:
                        continue
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            if level:
                res.append(level[0])
        return res
            

