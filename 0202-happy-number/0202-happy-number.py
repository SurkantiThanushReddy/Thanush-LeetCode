class Solution:
    def isHappy(self, n: int) -> bool:
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

        

       
        