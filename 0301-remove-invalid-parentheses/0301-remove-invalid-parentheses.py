class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = {s}

        while queue:
            valid = []

            # Check all strings at the current removal level
            for string in queue:
                if is_valid(string):
                    valid.append(string)

            # If we found valid strings, this is the minimum
            # number of removals.
            if valid:
                return valid

            # Generate strings by removing one parenthesis
            next_level = set()

            for string in queue:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i + 1:])

            queue = next_level

        return [""]