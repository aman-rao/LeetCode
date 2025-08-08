class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True

        def isSame(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        def dfs(node):
            if not node:
                return False
            
            if isSame(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
