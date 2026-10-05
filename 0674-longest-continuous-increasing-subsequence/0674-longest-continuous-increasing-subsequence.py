class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        cnt=0
        ans=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                cnt+=1
                ans=max(cnt,ans)
            else:
                cnt=0
        return ans+1