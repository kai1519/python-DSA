class Solution:
    def maxProduct(self, nums: List[int]) -> int:
     minv =maxv= ans =nums[0]
     for i in  range(1,len(nums)):
        d=nums[i]
        temp_max=max(maxv *d, minv*d,d)
        temp_min =min(maxv*d,minv*d,d)
        maxv=temp_max
        minv= temp_min
        ans =max(ans,maxv)
     return ans