class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #recursive
        if not root:
            return []
        stack=[]
        result=[]
        cur=root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            result.append(cur.val)
            if cur.right:
                cur=cur.right
                stack.append(cur.right)    
        return result
#------------------------------
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative method 1 (modifed from inorder iterative method)
        if not root:
            return []
        stack=[]
        result=[]
        cur=root
        while stack or cur:
            while cur:
                
                result.append(cur.val)
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            cur=cur.right
        return result
    