class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_map = {}
        for number in nums:
            if number in frequency_map:
                frequency_map[number] += 1
            else:
                frequency_map[number] = 1

        frequent_elements = []
        while len(frequent_elements) < k:
            max_freq = -1
            max_num = None
            for num, freq in frequency_map.items():
                if freq > max_freq and num not in frequent_elements:
                    max_freq = freq
                    max_num = num
            frequent_elements.append(max_num)

        return frequent_elements
