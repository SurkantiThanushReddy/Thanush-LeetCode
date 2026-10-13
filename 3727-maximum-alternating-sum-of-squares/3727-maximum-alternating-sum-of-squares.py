class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        li=[]
        for i in nums:
            li.append(abs(i))
        li.sort(reverse=True)
        res=[0]*len(nums)
        l=0
        r=len(nums)-1
        for i in range(len(nums)):
            if i%2==0:
                res[i]=li[l]
                l+=1
            else:
                res[i]=li[r]
                r-=1
        s=0
        for i in range(len(li)):
            if i%2==0:
                s+=res[i]**2
            else:
                s-=res[i]**2
        return s
