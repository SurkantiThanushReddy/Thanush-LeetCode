class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        ans=0
        my={}
        for r in range(len(s)):
            my[s[r]]=my.get(s[r],0)+1
            while (r-l+1)-max(my.values())>k:
                my[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans