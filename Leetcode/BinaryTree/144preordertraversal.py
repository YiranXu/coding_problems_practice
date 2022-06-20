class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative
        
        if not root:
            return
        stack,output=[root,],[]
        while stack:
            root=stack.pop()
            if root:
                output.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return output
#---------------------------
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        def preorder(root):
            if not root:
                return
            result.append(root.val)
            preorder(root.left)
            preorder(root.right)
        result=[]
        preorder(root)
        return result
        