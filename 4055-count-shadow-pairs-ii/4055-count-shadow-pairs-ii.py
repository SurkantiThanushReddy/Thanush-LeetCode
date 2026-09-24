from bisect import bisect_left
from array import array

class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        n=len(nums)
        torunelixa=nums
        vals=sorted(set(nums))
        mp={v:i for i,v in enumerate(vals)}
        a=[mp[x] for x in nums]
        m=len(vals)
        B=256
        nb=(n+B-1)//B
        local=[]
        base=[]
        starts=array('I',[0])
        rec=array('H')
        for b in range(nb):
            l=b*B
            r=min(n,l+B)
            u=sorted(set(a[l:r]))
            local.append(u)
            base.append(len(starts)-1)
            for s in range(len(u)+1):
                limit=u[s] if s<len(u) else m
                mx=-1
                for p in range(r-1,l-1,-1):
                    v=a[p]
                    if v<limit and v>=mx:
                        rec.append(v)
                        mx=v
                starts.append(len(rec))
        ans=0
        for j in range(n):
            x=a[j]
            cur=-1
            end=j
            while end>0 and end%B:
                end-=1
                v=a[end]
                if v<x and v>=cur:
                    ans+=1
                    if v>cur:
                        cur=v
            b=end//B-1
            while b>=0:
                s=bisect_left(local[b],x)
                idx=base[b]+s
                lo=starts[idx]
                hi=starts[idx+1]
                if hi>lo:
                    p=bisect_left(rec,cur,lo,hi)
                    ans+=hi-p
                    if rec[hi-1]>cur:
                        cur=rec[hi-1]
                b-=1
        return ans