class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixsum=[0]*(len(gain)+1)
        for i in range(1,len(gain)+1):
            prefixsum[i]=prefixsum[i-1]+gain[i-1]
        return max(prefixsum)
        
