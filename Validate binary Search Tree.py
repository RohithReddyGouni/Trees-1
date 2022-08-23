# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.bstList=[]
        self.inorder(root)
        for i in range(1,len(self.bstList)):
            if self.bstList[i]>self.bstList[i-1]:
                continue
            else:
                return False
        return True
    def inorder(self,root):
        #base condition
        if root==None:
            return
        self.inorder(root.left)
        #stack.pop()
        print("UP at line 23")
        print("root.val at 24",root.val)
        
        ###This is where root goes inside the bstList
        self.bstList.append(root.val)
        print("bstList=",self.bstList)
        self.inorder(root.right)
        #stack.pop()
        print("DOWN at line 30")
        print("root.val at line 31",root.val)
        