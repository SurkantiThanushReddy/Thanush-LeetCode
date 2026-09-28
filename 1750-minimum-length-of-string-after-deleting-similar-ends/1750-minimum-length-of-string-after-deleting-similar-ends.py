class Solution:
    def minimumLength(self,s:str)->int:
        l=0
        r=len(s)-1
        cnt=len(s)
        while l<r:
            if s[l]==s[r]:
                ch=s[l]
                while l<=r and s[l]==ch:
                    l+=1
                while l<=r and s[r]==ch:
                    r-=1
                cnt=r-l+1
            else:
                break
        return cnt