class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=sorted(nums1+nums2)
        if len(merged)%2!=0:
            ans=float(merged[int(len(merged)/2)])
        else:
            ans=float((merged[int((len(merged)-1)/2)]+merged[int(len(merged)/2)])/2)
        return ans
        