class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        sp=[]
        for i in range(n):
            if n%(i+1)==0:
                sp.append(nums[i])
        print(sp)
        sum=0
        for i in sp:
            sum+=i**2
        return sum
