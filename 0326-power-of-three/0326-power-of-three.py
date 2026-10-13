class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n<=0:
        #     return False
        # s=0
        # for i in range(int(n/3)+1):
        #     s=3**i
        #     if s==n :
        #         print(s)
        #         return True
        # return False
        if n<=0:
            return False

        while n % 3 == 0:
            n//=3

        return n==1