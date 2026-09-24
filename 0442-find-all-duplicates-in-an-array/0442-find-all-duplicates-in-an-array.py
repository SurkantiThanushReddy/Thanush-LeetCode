class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mydict={}
        for i in nums:
            mydict[i]=mydict.get(i,0)+1
        res=[]
        for key,value in mydict.items():
            if value==2:
                res.append(key)
        return res
