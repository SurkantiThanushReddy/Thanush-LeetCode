class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        # l=0
        # k1=k
        # r=len(cardPoints)-1
        # r1=len(cardPoints)-1
        # l1=0
        # s=0
        # while k!=0:
        #     if cardPoints[l]==cardPoints[r]:
        #         s+=cardPoints[l]
        #         l+=1
        #         k-=1
        #     elif cardPoints[l]>cardPoints[r]:
        #         s+=cardPoints[l]
        #         l+=1
        #         k-=1
        #     elif cardPoints[l]<cardPoints[r]:
        #         s+=cardPoints[r]
        #         r-=1
        #         k-=1
        # s2=0
        # while k1!=0:
        #     if cardPoints[l1]==cardPoints[r1]:
        #         s2+=cardPoints[r1]
        #         r1-=1
        #         k1-=1
        #     elif cardPoints[l1]>cardPoints[r1]:
        #         s2+=cardPoints[l1]
        #         l1+=1
        #         k1-=1
        #     elif cardPoints[l1]<cardPoints[r1]:
        #         s2+=cardPoints[r1]
        #         r1-=1
        #         k1-=1
        # return max(s,s2)
        # s=sum(cardPoints[:k])
        # ans=s
        # for i in range(1,k+1):
        #     s-=cardPoints[k-i]
        #     s+=cardPoints[-i]
        #     ans=max(ans, s)
        # return ans
        n=len(cardPoints)
        currSum=sum(cardPoints[n-k::])
        print(currSum)
        ans=currSum
        for i in range(k):
            currSum+=cardPoints[i]
            currSum-=cardPoints[n-k+i]
            if currSum>ans:
                ans=currSum
        return ans
