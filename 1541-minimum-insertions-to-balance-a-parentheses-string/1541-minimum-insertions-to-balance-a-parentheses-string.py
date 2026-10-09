class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        open = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                open += 1

            else:
                # Check whether we have a pair of ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    # Insert one ')' to complete the pair
                    ans += 1

                # Match the pair '))' with an opening '('
                if open > 0:
                    open -= 1
                else:
                    # Insert '(' because no opening bracket exists
                    ans += 1

            i += 1

        # Each unmatched '(' needs two closing parentheses
        return ans + 2 * open