class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mydict={}
        for i in nums:
            mydict[i]=mydict.get(i,0)+1
        for key,value in mydict.items():
            if value==1:
                return key
