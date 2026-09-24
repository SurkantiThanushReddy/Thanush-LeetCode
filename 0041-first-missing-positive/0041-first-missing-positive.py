class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # mini=1
        # maxi=max(nums)
        # s=set(nums)
        # if maxi<0:
        #     return 1
        # else:
        #     for i in range(mini,maxi):
        #         if i not in s:
        #             return i
        #     return maxi+1
        n=set(nums)
        for i in range(1,len(nums)+2):
            if i not in n:
                return i
        return len(nums)+1
