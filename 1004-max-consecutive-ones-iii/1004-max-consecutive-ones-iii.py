class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=0
        ans=0
        r=0
        for i in range(len(nums)):
            if nums[i]==0:
                r+=1
            while r>k:
                if nums[l]==0:
                    r-=1
                l+=1
            ans=max(ans,i-l+1)
        return ans
