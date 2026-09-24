class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        count = 1

        for i in range(len(chars)):
            if i + 1 < len(chars) and chars[i] == chars[i + 1]:
                count += 1
            else:
                res.append(chars[i])

                if count > 1:
                    for j in str(count):
                        res.append(j)

                count = 1

        chars[:] = res
        return len(res)