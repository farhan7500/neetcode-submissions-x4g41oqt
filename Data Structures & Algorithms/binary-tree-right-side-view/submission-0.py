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
        result = []
        queue = collections.deque([root])
        while queue:
            queue_len = len(queue)
            visible = None
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    visible = node.val
                    queue.append(node.left)
                    queue.append(node.right)
            if visible:
                result.append(visible)
        return result


