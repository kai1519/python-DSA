from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        s = 1

        # Prefix products
        for i in range(1, len(nums)):
            ans[i] = nums[i - 1] * ans[i - 1]

        # Suffix products
        for j in range(len(nums) - 2, -1, -1):
            s = s * nums[j + 1]
            ans[j] = ans[j] * s

        return ans

