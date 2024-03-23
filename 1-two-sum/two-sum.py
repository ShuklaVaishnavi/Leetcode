class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev={}
        for i,n in enumerate(nums):
            d=target-n
            if d in prev:
                return(prev[d],i)
            prev[n]=i