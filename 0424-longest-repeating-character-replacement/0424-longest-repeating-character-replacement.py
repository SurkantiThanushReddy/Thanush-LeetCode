class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        ans=0
        my={}
        for i in range(len(s)):
            my[s[i]]=my.get(s[i],0)+1
            while (i-l+1)-max(my.values())>k:
                my[s[l]]-=1
                l+=1
            ans=max(ans,i-l+1)
        return ans