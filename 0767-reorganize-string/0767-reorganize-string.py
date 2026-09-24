class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        for i in s:
            freq[i] = freq.get(i, 0) + 1

        res = ""

        while freq:
            key = max(freq, key=freq.get)

            if res and res[-1] == key:
                key = ""
                for i in freq:
                    if i != res[-1]:
                        key = i
                        break

                if key == "":
                    return ""

            res += key
            freq[key] -= 1

            if freq[key] == 0:
                del freq[key]

        return res