class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=0
        cnt=0
        mdict={0:1}
        for i in nums:
            prefix+=i
            rem=prefix%k
            cnt+=mdict.get(rem,0)
            mdict[rem]=mdict.get(rem,0)+1
        return cnt