from collections import Counter
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        if len(basket1)!=len(basket2):
            return -1
        else:
            bc1=Counter(basket1)
            bc2=Counter(basket2)
            B=bc1+bc2
            for k,v in B.items():
                if v%2==1:
                    return -1
        xtra1=[]
        xtra2=[]
        for i in B:
            diff=bc1[i]-bc2[i]
            if diff<0:
                xtra2.extend([i]*((-diff)//2))
            elif diff>0:
                xtra1.extend([i]*(diff//2))
            else:
                continue
        # # xtra1.sort()
        # # xtra2.sort(reverse=True)
        # print(xtra1)
        # print(xtra2)
        # res=0
        # for i in range(len(xtra1)):
        #     res+=min(xtra1[i],xtra2[i])       
        # return res
        xtra1.sort(reverse=True)
        xtra2.sort()
        res=0
        mn=min(B)
    
        for i in range(len(xtra1)):
            res+=min(xtra1[i],xtra2[i],2*mn)
        return res
            