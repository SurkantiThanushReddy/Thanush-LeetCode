class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len=float('inf')
        curr_sum=0
        start=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            while curr_sum>=target:
                min_len=min(min_len,i-start+1)
                curr_sum-=nums[start]
                start+=1
        if min_len==float('inf'):
            return 0
        else:
            return min_len
        
