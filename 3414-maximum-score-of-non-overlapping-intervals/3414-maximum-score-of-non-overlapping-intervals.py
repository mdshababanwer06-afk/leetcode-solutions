class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store: (start, end, weight, original_index)
        a = [
            (s, e, w, i)
            for i, (s, e, w) in enumerate(intervals)
        ]

        # Sort by start, then end, weight, index
        a.sort()

        starts = [x[0] for x in a]

        # next[i] = first interval with start > a[i].end
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_right(starts, a[i][1])

        @lru_cache(None)
        def dp(i, k):
            if i == n or k == 0:
                return (0, ())

            # Skip current interval
            best = dp(i + 1, k)

            # Take current interval
            w = a[i][2]
            idx = a[i][3]

            take_score, take_indices = dp(nxt[i], k - 1)

            take = (
                take_score + w,
                tuple(sorted(take_indices + (idx,)))
            )

            # Maximize score, then lexicographically smallest indices
            if take[0] > best[0]:
                return take

            if take[0] < best[0]:
                return best

            return min(take, best, key=lambda x: x[1])

        return list(dp(0, 4)[1])