class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(numbers)):
            tar=target-numbers[i]
            if tar not in hash:
                hash[numbers[i]]=i
            else:
                return [hash[tar]+1,i+1]