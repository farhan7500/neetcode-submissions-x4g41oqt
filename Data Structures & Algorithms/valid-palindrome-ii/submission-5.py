class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0 , len(s) - 1

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
            

        while left < right:
            if s[left] != s[right]:
                return is_palindrome(left, right - 1) or is_palindrome(left + 1, right)
            left += 1
            right -= 1
        return True

