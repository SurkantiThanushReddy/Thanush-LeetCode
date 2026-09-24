class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority,votes=nums[0],1
        for i in range(1,len(nums)):
            if votes==0:
                votes+=1
                majority=nums[i]
            elif nums[i]==majority:
                votes+=1
            else:
                votes-=1
        return majority