class Solution:
    def productExceptSelf(self,nums:List[int])->List[int]:
        preproduct=[1]*len(nums)
        for i in range(1,len(nums)):
            preproduct[i]=preproduct[i-1]*nums[i-1]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            preproduct[i]=preproduct[i]*suffix
            suffix=suffix*nums[i]
        return preproduct