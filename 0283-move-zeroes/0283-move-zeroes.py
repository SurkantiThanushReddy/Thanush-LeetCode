class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i,k=0,0
        for i in range(len(nums)):
            if nums[i]==0:
                continue
            else:
                nums[k]=nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[i]=0



        """
        Do not return anything, modify nums in-place instead.
        """
        