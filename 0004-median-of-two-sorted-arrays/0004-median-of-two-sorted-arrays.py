class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array = sorted(nums1+nums2)
        n = len(merged_array)
        m = n // 2
        if n % 2 == 0:
            middle_sum = merged_array[m-1] + merged_array[m]

            return middle_sum / 2

        else:
            return float(merged_array[m])