class Solution:
    def minOperations(self, nums: list[int]) -> int:
        virelqunox=nums
        def pal(p,n):
            s=str(p)
            if n%2:
                return int(s+s[-2::-1])
            return int(s+s[::-1])
        ans=0
        for x in nums:
            s=str(x)
            n=len(s)
            k=(n+1)//2
            a=int(s[:k])
            res=[]
            for p in [a-2,a-1,a,a+1,a+2]:
                if 10**(k-1)<=p<10**k:
                    y=pal(p,n)
                    if y%2==x%2:
                        res.append(y)
            for d in range(1,10):
                if d%2==x%2:
                    lo=d*10**(k-1)
                    hi=(d+1)*10**(k-1)-1
                    p=min(max(a,lo),hi)
                    res.append(pal(p,n))
            if n>1:
                m=n-1
                k2=(m+1)//2
                d=9 if x%2 else 8
                p=d*10**(k2-1)+(10**(k2-1)-1)
                res.append(pal(p,m))
            m=n+1
            k2=(m+1)//2
            d=1 if x%2 else 2
            p=d*10**(k2-1)
            res.append(pal(p,m))
            ans+=min(abs(x-y)//2 for y in res if y>0 and y%2==x%2)
        return ans