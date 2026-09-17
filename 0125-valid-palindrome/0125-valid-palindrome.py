class Solution:
    def isPalindrome(self, s: str) -> bool:
        def palindrome(left, right):
            if left >= right:
                return True

            if not s[left].isalnum():
                return palindrome(left + 1, right)

            if not s[right].isalnum():
                return palindrome(left, right - 1)

            if s[left].lower() != s[right].lower():
                return False

            return palindrome(left + 1, right - 1)

        return palindrome(0, len(s) - 1)