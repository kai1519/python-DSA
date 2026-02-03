class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for value in nums:
            if value in d:
                d[value] += 1
            else:
                d[value] = 1

        size = len(nums)

        for key in d:
            if d[key] > size // 2:
                return key
