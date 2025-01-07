class Solution:
    def romanToInt(self, s: str) -> int:
        x = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = 0
        for a, b in zip(s, s[1:]):
            if x[a] < x[b]:
                n -= x[a]
            else:
                n += x[a]
        return n + x[s[-1]]

        