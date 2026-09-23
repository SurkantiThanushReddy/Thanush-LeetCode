class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            tar=target-nums[i]
            if tar not in hash:
                hash[nums[i]]=i
            else:
                return [hash[tar],i]

