class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hm = {}
        size = -(len(nums2))
        index = -1
        while index >= size:
            data = nums2[index]
            while stack:
                if data < stack[-1]:
                    hm[data] = stack[-1]
                    break
                else:
                    stack.pop()
            if not stack:
                hm[data] = -1
            stack.append(data)
            index -= 1
        ans = []
        for val in nums1:
            ans.append(hm[val])
        return ans