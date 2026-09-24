class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=set(nums)
        res=list(sorted(a))
        for i in range(len(res)):
            nums[i]=res[i]
        return len(res)
