class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        strs = [str(num) for num in nums]
        
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0
            
        strs.sort(key=cmp_to_key(compare))
        
        if strs[0] == "0":
            return "0"
            
        return "".join(strs)