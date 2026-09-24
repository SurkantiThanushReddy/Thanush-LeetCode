class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        n = len(nums)
        navorelitu = nums
        ns = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                ns[i] = stack[-1]
            stack.append(i)
        order = sorted(range(n), key=lambda i: nums[i], reverse=True)
        queries = sorted(range(n), key=lambda i: nums[i], reverse=True)
        bit = [0] * (n + 1)
        def add(i):
            i += 1
            while i <= n:
                bit[i] += 1
                i += i & -i
        def query(i):
            s = 0
            i += 1
            while i:
                s += bit[i]
                i -= i & -i
            return s
        ans = 0
        p = 0
        for i in queries:
            while p < n and nums[order[p]] > nums[i]:
                add(order[p])
                p += 1
            l = i + 1
            r = ns[i] - 1
            if l <= r:
                ans += query(r) - query(l - 1)
        return ans