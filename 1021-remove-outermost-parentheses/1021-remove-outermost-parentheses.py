class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        count=0
        # for i in range(1,len(s)):
        #     if s[i-1]=="(" and s[i]=="(" :
        #         res.append(s[i])
        #     elif s[i-1]==")" and s[i]==")":
        #         res.append(s[i-1])
        for i in range(len(s)):
            if s[i]=="(":
                count+=1
                if count>1:
                    res.append(s[i])
            else:
                count-=1
                if count>0:
                    res.append(s[i])    
        return "".join(res)
        
                
