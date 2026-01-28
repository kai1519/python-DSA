class Solution:
    def maxArea(self, height: List[int]) -> int:
        start= 0
        end =len(height)-1
        result=0 
        while start < end:
            w=end-start
            h=min(height[start],height[end])
            ans=w*h
            result=max(result,ans)
            if height[start]<height[end]:
                start +=1    
            else:
                end-=1      
        return result