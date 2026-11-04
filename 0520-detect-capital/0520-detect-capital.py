class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(i.isupper() for i in word):
            return True
        elif all(i.islower()for i in word):
            return True
        elif word[0].isupper() and all(i.islower() for i in word[1:]):
            return True
        
        return False