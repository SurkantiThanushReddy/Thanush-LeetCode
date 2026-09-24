class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res=[""]      
        for i in s:
            new_res=[]        
            if i.isalpha():
                for j in res:
                    new_res.append(j+i.lower())
                    new_res.append(j+i.upper())
            else:
                for j in res:
                    new_res.append(j+i)     
            res=new_res       
        return res
