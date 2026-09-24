# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val: i for i, val in enumerate(inorder)}
        preorderIndex = 0

        def helper(left, right):
            nonlocal preorderIndex

            if left > right:
                return None

            rootVal = preorder[preorderIndex]
            preorderIndex += 1

            root = TreeNode(rootVal)
            mid = inorderMap[rootVal]

            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)