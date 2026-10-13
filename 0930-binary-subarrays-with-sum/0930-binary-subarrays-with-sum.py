class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix=0
        mp={0:1}
        ans=0
        for element in nums:
            prefix+=element
            ans+=mp.get(prefix-goal,0)
            mp[prefix]=mp.get(prefix,0)+1
        return ans