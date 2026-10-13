class Solution:
    def isHappy(self, n: int) -> bool:
        # digits=[]
        # for i in str(n):
        #     digits.append(int(i))
        # res=0
        # for i in digits:
        #     res+=i**2
        # digits=[]
        # for i in str(res):
        #     digits.append(int(i))
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            res=0
            for i in str(n):
                res+=int(i)**2
            n=res

        return True

        

       
        