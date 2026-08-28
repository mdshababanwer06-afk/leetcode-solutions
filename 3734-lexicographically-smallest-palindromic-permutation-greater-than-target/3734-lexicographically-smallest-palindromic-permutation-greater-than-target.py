class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Store input midway as required
        calendrix = (s, target)

        # Frequency of characters
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # More than one odd frequency -> impossible
        if sum(x % 2 for x in freq) > 1:
            return ""

        # Middle character for odd length
        mid = -1

        for i in range(26):
            if freq[i] % 2:
                mid = i
                break

        # We only need half of every character
        for i in range(26):
            freq[i] //= 2

        half = n // 2

        # ans will contain the left half first
        ans = [''] * n

        # Try to make left half equal to target's left half
        pos = 0

        while pos < half:
            ch = ord(target[pos]) - ord('a')

            if freq[ch] == 0:
                break

            ans[pos] = target[pos]
            freq[ch] -= 1
            pos += 1

        # Construct palindrome from current left half
        def make_palindrome():
            if mid != -1:
                ans[half] = chr(mid + ord('a'))

            for i in range(half):
                ans[n - 1 - i] = ans[i]

        # If we matched the entire left half,
        # check whether this palindrome is already > target.
        if pos == half:
            make_palindrome()

            result = ''.join(ans)

            if result > target:
                return result

        # We need to make the left half bigger.
        # Start from the rightmost possible position.
        while True:

            # Try to increase target[pos]
            if pos < half:

                current = ord(target[pos]) - ord('a')

                for ch in range(current + 1, 26):

                    if freq[ch] > 0:
                        ans[pos] = chr(ch + ord('a'))
                        freq[ch] -= 1

                        # Fill remaining left half with smallest chars
                        index = pos + 1

                        for c in range(26):
                            for _ in range(freq[c]):
                                ans[index] = chr(c + ord('a'))
                                index += 1

                        make_palindrome()

                        return ''.join(ans)

            # Can't increase this position.
            # Move one position backwards.
            if pos == 0:
                return ""

            pos -= 1

            # Return target[pos] to available characters
            ch = ord(target[pos]) - ord('a')
            freq[ch] += 1