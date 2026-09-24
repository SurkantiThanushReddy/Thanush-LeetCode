class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # d={}
        # for i in nums:
        #     d[i]=d.get(i,0)+1
        # for key,value in d.items():
        #     if value==1:
        #         return key
        def unique(nums):
            xor=0
            for i in nums:
                xor^=i
            return xor
        return unique(nums)
        
