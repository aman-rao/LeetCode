class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(openP, closeP, s):
            if openP == closeP and openP + closeP == 2 * n:
                result.append(s)
                return

            if openP < n:
                dfs(openP + 1, closeP, s + "(")

            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")
            
        dfs(0, 0, "")

        return result
