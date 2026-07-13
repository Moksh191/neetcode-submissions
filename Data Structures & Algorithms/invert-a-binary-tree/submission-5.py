# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        
        node_queue = []
        node_queue.append(root)

        while node_queue:
            curr = node_queue.pop()
            temp = curr.right
            curr.right = curr.left
            curr.left = temp
            if curr.left:
                node_queue.append(curr.left)
            if curr.right:
                node_queue.append(curr.right)
      
        
        return root
