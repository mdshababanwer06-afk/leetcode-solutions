class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        current = []

        
        def  backtrack(i):

            if i == len(nums):
                result.append(current.copy())
                return

            backtrack(i+1)

            current.append(nums[i])
            backtrack(i +1)

            current.pop()

        backtrack(0)

        return result

