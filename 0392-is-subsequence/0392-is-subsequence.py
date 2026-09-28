class Solution:
    def isSubsequence(self,s:str,t:str)->bool:
        cnt=0
        for i in t:
            if cnt<len(s) and i==s[cnt]:
                cnt+=1
        return cnt==len(s)