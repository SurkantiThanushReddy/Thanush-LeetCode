class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start=max(arriveAlice,arriveBob)
        end=min(leaveAlice,leaveBob)
        if start>end:
            return 0
        sm,sd=map(int,start.split('-'))
        em,ed=map(int,end.split('-'))
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        s=sum(days[:sm-1])+sd
        e=sum(days[:em-1])+ed
        return e-s+1