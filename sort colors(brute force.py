class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(0, len(nums) - 1):
            for j in range(0, len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
# Time complexity: O(n^2)