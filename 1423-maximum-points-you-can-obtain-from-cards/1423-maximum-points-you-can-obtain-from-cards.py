class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
           return sum(cardPoints)

        left_Sum = 0
        right_Sum = 0
        for i in range(0,k):
            left_Sum += cardPoints[i]
        maxi = left_Sum
        right_index = n-1
        for i in range(k-1,-1,-1):
            left_Sum -= cardPoints[i]
            right_Sum += cardPoints[right_index]
            maxi = max(maxi,right_Sum+left_Sum)
            right_index -= 1
        return maxi 