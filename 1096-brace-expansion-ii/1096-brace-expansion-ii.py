class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(s):
            result = {""}
            i = 0

            while i < len(s):

                # Bracket expression
                if s[i] == '{':
                    count = 1
                    j = i + 1

                    while count > 0:
                        if s[j] == '{':
                            count += 1
                        elif s[j] == '}':
                            count -= 1
                        j += 1

                    inside = s[i + 1:j - 1]

                    # Split by top-level comma
                    parts = []
                    start = 0
                    count = 0

                    for k in range(len(inside)):
                        if inside[k] == '{':
                            count += 1
                        elif inside[k] == '}':
                            count -= 1
                        elif inside[k] == ',' and count == 0:
                            parts.append(inside[start:k])
                            start = k + 1

                    parts.append(inside[start:])

                    # Union
                    choices = set()

                    for part in parts:
                        choices.update(parse(part))

                    i = j

                else:
                    choices = {s[i]}
                    i += 1

                # Concatenation
                new_result = set()

                for a in result:
                    for b in choices:
                        new_result.add(a + b)

                result = new_result

            return result

        return sorted(parse(expression))