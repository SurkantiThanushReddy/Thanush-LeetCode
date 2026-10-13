class Solution:
    def addDigits(self, num: int) -> int:
        digits=[]
        for i in str(num):
            digits.append(int(i))
        while len(digits)!=1:
            s=0
            for i in digits:
                s+=i
            digits=[]
            for i in str(s):
                digits.append(int(i))
        return digits[0]
        