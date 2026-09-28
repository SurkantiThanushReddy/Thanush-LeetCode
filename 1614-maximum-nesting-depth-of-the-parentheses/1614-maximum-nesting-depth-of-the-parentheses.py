class Solution:
    def maxDepth(self, s: str) -> int:
        r=[]
        cnt=0
        max_cnt=0
        for i in s:
            if i=="(":
                r.append(i)
                cnt+=1
            if i==")":
                r.pop()
                cnt-=1
            max_cnt=max(max_cnt,cnt)
        return max_cnt