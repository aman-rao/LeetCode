class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest_string_length = 0
        frequency = {}

        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1
            longest_string_length = max(longest_string_length, frequency[s[right]])

            if right - left + 1 - longest_string_length > k:
                frequency[s[left]] -= 1
                left += 1
        
        return len(s) - left
