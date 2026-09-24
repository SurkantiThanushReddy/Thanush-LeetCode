# from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # mst=dict(Counter(nums).most_common(k))
        # res=[]
        # for i in mst:
        #     res.append(i)
        # return res
        md={}
        res=[]
        for i in nums:
            md[i]=md.get(i,0)+1
        md=sorted(md,key=lambda x:md[x],reverse=True)
        for i in range(k):
            res.append(md[i])
            
        return res

