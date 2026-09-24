class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        if digits[-1]<9:
            for i in range(len(digits)):
                res.append(digits[i])
            res[-1]+=1
            return res
        for i in range(len(digits)):
            res.append(digits[i])
        i=len(res)-1
        while i>=0 and res[i]== 9:
            res[i] = 0
            i-=1
        if i < 0:
            res.insert(0,1)
        else:
            res[i]+=1
        return res