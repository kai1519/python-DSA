from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        size = len(nums)
        result = []
        for x in range(size):
            if x > 0 and nums[x] == nums[x -1]:
                continue
            for y in range(x+1, size):
                if y > x+1 and nums[y] == nums[y -1]:
                    continue

                start = y+1
                end = size -1

                while start < end:
                    sum = nums[x] + nums[y] + nums[start] + nums[end]

                    if sum == target:
                        result.append([nums[x] , nums[y] , nums[start] , nums[end]])

                        start += 1
                        end -= 1

                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif sum < target:
                        end -= 1
                    else:
                        start += 1
        return result