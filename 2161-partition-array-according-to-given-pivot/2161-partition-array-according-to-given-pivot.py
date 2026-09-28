class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        l=[]
        r=[]
        m=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                l.append(nums[i])
            elif nums[i]==pivot:
                m.append(nums[i])
            else:
                r.append(nums[i])
        return l+m+r