class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = count1 = count2 = 0
        index = 0

        for value in nums:
            if value == 0:
                count0 += 1
            elif value == 1:
                count1 += 1
            else:
                count2 += 1

        while index < len(nums):
            if index < count0:
                nums[index] = 0
            elif index < count0 + count1:
                nums[index] = 1
            else:
                nums[index] = 2
            index += 1
