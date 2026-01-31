from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        result = []

        for x in range(size - 3):
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            for y in range(x + 1, size - 2):
                if y > x + 1 and nums[y] == nums[y - 1]:
                    continue

                start = y + 1
                end = size - 1

                while start < end:
                    total = nums[x] + nums[y] + nums[start] + nums[end]

                    if total == target:
                        result.append([nums[x], nums[y], nums[start], nums[end]])
                        start += 1
                        end -= 1

                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1

                    elif total < target:
                        start += 1   
                    else:
                        end -= 1     

        return result
