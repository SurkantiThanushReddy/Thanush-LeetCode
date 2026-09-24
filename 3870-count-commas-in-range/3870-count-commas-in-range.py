class Solution:
    def countCommas(self, n: int) -> int:
        ans=0
        start=1000
        while start<=n:
            ans=ans+n-start+1
            start=start*10**3
        return ans
