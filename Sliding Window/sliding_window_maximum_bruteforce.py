class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1
        max_list = []
        max_element = nums[0]

        while right < len(nums):
            max_element = max(nums[left::right+1])
            max_list.append(max_element)
            left+= 1
            right += 1
        return max_list
