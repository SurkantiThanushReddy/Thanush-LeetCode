class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq={}
        if k>len(nums):
            return 0
        current_sum=0
        max_sum=0
        for i in range(k):
            current_sum+=nums[i]
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        if len(freq) == k:
            max_sum = current_sum
        for i in range(len(nums)-k):
            left=nums[i]
            current_sum-=left
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]
            right = nums[i+k]
            current_sum += right
            freq[right] = freq.get(right, 0) + 1
            if len(freq) == k:
                max_sum = max(max_sum, current_sum)
        return max_sum

