from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mst=dict(Counter(nums).most_common(k))
        res=[]
        for i in mst:
            res.append(i)
        return res

