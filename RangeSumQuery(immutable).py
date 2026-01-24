class NumArray:

    def __init__(self, nums: List[int]):
        self.num =nums

    def sumRange(self, left: int, right: int) -> int:
        sum=0
        while left <= right:
            sum+=self.num[left]
            left+=1
        return sum   