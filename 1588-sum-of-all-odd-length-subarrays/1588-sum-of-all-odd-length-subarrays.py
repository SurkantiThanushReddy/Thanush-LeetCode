class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total=0
        for i in range(len(arr)):
            s=0
            for j in range(i,len(arr)):
                s+=arr[j]
                if (j-i+1)%2==1:
                    total+=s
        return total