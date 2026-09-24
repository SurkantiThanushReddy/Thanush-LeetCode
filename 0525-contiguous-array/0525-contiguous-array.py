class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        prefix=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                prefix[i]=nums[i]
            else:
                prefix[i]=prefix[i-1]+nums[i]
        freq = {0: -1}
        max_len = 0

        for i in range(len(prefix)):
            if prefix[i] in freq:
                length = i - freq[prefix[i]]
                max_len = max(max_len, length)
            else:
                freq[prefix[i]] = i

        return max_len

                