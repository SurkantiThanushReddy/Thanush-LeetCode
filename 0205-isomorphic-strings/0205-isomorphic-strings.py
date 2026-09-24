class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for i in range(len(s)):
            a=s[i]
            b=t[i]

            if a in sd and sd[a]!=b:
                return False

            if b in td and td[b]!=a:
                return False

            sd[a]=b
            td[b]=a

        return True
