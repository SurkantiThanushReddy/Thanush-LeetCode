class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1={}
        d2={}
        for i in ransomNote:
            d1[i]=d1.get(i,0)+1
        for i in magazine:
            d2[i]=d2.get(i,0)+1
        for i in d1:
            if i not in d2:
                return False
            if d1[i] > d2[i]:
                return False

        return True