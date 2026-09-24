class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt={}
        for i in s:
            cnt[i]=cnt.get(i,0)+1
        res=""
        for i in order:
            if i in cnt:
                for _ in range(cnt[i]):
                    res+=i
                cnt[i]=0       
        for i in s:
            if cnt[i]>0:
                for _ in range(cnt[i]):
                    res += i
                cnt[i]=0
        return res            
