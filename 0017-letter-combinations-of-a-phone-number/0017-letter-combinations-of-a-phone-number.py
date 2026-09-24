class Solution:
    def letterCombinations(self,digits:str)->list[str]:
        mydict={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if not digits:
            return []
        res=[""]
        for digit in digits:
            temp=[]
            for x in res:
                for ch in mydict[digit]:
                    temp.append(x+ch)
            res=temp
        return res