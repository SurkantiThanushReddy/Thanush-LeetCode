class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat=[]
        for i in range(len(pattern)):
            pat.append(pattern[i])
        sl=s.split(" ")
        if len(pat)!=len(sl):
            return False
        if len(list(set(pat)))!=len(list(set(sl))):
            return False
        mapping = {}
        for i in range(len(pat)):
            if pat[i] in mapping:
                if mapping[pat[i]]!=sl[i]:
                    return False
            else:
                mapping[pat[i]] = sl[i]
        return True
