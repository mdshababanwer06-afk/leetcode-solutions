class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # Find the rightmost position where we can make
        # target[i] slightly bigger.
        possible = -1

        temp = count[:]

        for i in range(len(target)):
            x = ord(target[i]) - ord('a')

            # Is there any character bigger than target[i] available?
            for c in range(x + 1, 26):
                if temp[c] > 0:
                    possible = i
                    break

            # Try to match target[i]
            if temp[x] == 0:
                break

            temp[x] -= 1

        if possible == -1:
            return ""

        # Use the original count again.
        result = []

        # Put target's prefix before 'possible'
        for i in range(possible):
            result.append(target[i])
            count[ord(target[i]) - ord('a')] -= 1

        # At 'possible', use the smallest character > target[possible]
        x = ord(target[possible]) - ord('a')

        for c in range(x + 1, 26):
            if count[c] > 0:
                result.append(chr(c + ord('a')))
                count[c] -= 1
                break

        # Put all remaining characters in sorted order
        for c in range(26):
            result.extend([chr(c + ord('a'))] * count[c])

        return ''.join(result)