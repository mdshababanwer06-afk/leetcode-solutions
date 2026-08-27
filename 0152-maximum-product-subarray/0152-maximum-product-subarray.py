class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        ans =nums[0]
        for i in range(1,len(nums)):
            x = nums[i]
            old_max = curr_max
            old_min = curr_min
            curr_max = max(x,x*old_max,x*old_min)
            curr_min = min(x,x*old_max,x*old_min)

            ans = max(ans,curr_max)
        return ans
