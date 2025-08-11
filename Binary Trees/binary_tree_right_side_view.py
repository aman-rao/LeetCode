class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()
        q.append(root)

        while q:
            right = None

            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
                
            if right:
                res.append(right.val)
        return res
