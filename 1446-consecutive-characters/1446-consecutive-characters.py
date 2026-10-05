class Solution:
    def maxPower(self, s: str) -> int:
        ans=1
        cnt=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                cnt+=1
                ans=max(cnt,ans)
            else:
                cnt=1
        return ans
        