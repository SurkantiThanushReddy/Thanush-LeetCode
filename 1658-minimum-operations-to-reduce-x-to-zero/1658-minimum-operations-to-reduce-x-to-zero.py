class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total=sum(nums)
        target=total-x
        left=0
        curr=0
        max_len=-1
        for i in range(len(nums)):
            curr+=nums[i]
            while curr>target and left<=i:
                curr-=nums[left]
                left+=1
            if curr==target:
                max_len=max(max_len,i-left+1)
        if max_len==-1:
            return -1
        return len(nums)-max_len
        
