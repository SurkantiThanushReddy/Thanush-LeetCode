class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefixsum=[0]*len(nums)
        for i in range(len(nums)):
            prefixsum[i]=prefixsum[i-1]+nums[i]
        return prefixsum