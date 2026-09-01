class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        curr_s = s
        n = len(curr_s)
        for i in range(0,n):
            if curr_s == goal:
                return True
            curr_s = curr_s[-1]+curr_s[:-1]
        return False