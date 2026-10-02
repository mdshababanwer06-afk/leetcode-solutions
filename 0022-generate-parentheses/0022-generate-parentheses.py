class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(path, open, close):
            # Complete valid string
            if len(path) == 2 * n:
                ans.append(path)
                return

            # Add '('
            if open < n:
                backtrack(path + '(', open + 1, close)

            # Add ')' only if there is an unmatched '('
            if close < open:
                backtrack(path + ')', open, close + 1)

        backtrack("", 0, 0)

        return ans