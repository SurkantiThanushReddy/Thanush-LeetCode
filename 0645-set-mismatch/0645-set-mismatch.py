class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        res=[]
        for i in range(len(nums)):
            if nums.count(nums[i])==2:
                res.append(nums[i])
                break
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
                break
        return res