class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        # Find first and last position of every character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i

            last[ch] = i

        intervals = []

        # Try to create a valid substring for each character
        for ch in first:
            left = first[ch]
            right = last[ch]

            i = left
            valid = True

            while i <= right:
                current = s[i]

                # This character appeared before left
                if first[current] < left:
                    valid = False
                    break

                # Expand right to include all occurrences
                right = max(right, last[current])

                i += 1

            if valid:
                intervals.append((left, right))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        answer = []
        end = -1

        # Select non-overlapping intervals
        for left, right in intervals:
            if left > end:
                answer.append(s[left:right + 1])
                end = right

        return answer