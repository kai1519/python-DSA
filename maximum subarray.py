class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue = nums[0]
        sum = 0

        for v in nums:
            sum += v
            maxValue = max(maxValue, sum)
            if sum < 0:
                sum = 0

        return maxValue