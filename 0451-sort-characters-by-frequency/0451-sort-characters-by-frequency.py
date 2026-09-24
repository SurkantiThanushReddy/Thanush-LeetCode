class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        print(freq)
        res=""
        while freq:
            max_freq=0
            max_char=""
            for key,value in freq.items():
                if value>max_freq:
                    max_freq=value
                    max_char=key
            res += max_char * max_freq
            del freq[max_char]
        return res
    