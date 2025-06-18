class Solution:
    def isPalindrome(self, s: str) -> bool:
        is_palindrome = []
        for c in s:
            if c.isalnum():
                is_palindrome.append(c.lower())
        return is_palindrome == is_palindrome[::-1]
