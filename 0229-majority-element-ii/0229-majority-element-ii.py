class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        hash={}
        res=[]
        for i in nums:
            hash[i]=hash.get(i,0)+1
        for key,value in hash.items():
            if value>n//3:
                res.append(key)
        return res