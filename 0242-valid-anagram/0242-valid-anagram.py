class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            d = {}

            for i in s:
                d[i] = d.get(i, 0) + 1

            flag = True

            for i in t:
                if i not in d or d[i] == 0:
                    flag = False
                    break
                d[i] -= 1

            if flag:
                return True
            else:
                return False