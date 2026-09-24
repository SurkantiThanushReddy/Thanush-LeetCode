class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for i in strs:
            w="".join(sorted(i))
            if w in freq:
                freq[w].append(i)
            else:
                freq[w]=[i]
    
        return list(freq.values())