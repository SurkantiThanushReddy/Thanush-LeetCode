class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        a=0
        res=[]
        for i in range(len(candies)):
            a=candies[i]+extraCandies
            if a>=max(candies):
                res.append(True)
            else:
                res.append(False)
        return res

