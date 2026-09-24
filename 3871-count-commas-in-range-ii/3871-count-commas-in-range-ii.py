class Solution:
    def countCommas(self, n: int) -> int:
        ans=0
        start=1000
        commas=1

        while start<=n:
            end=start*1000-1

            if end>n:
                end=n

            ans+=(end-start+1)*commas

            start=start*1000
            commas+=1

        return ans