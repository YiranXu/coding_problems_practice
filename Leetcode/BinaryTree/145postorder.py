class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        result=[]
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                result.append(root.val)
            return 
        postorder(root)
        return result
##=======================
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative (modify from preorder iterative solution)
        # (preorder: parent-left child-right child --> 
        # change child order: parent-right child-left child
        # reverse the result: left child -right child-parent)
        if not root:
            return []
        stack=[root,]
        result=[]
        cur=root
        while stack:
            cur=stack.pop()
            result.append(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return result[::-1]