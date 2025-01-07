class Solution:
    def isPalindrome(self, x: int) -> bool:
        import operator

        a = list(str(x))
        b = list(str(x))
        b.reverse()
        result = operator.eq(a, b)
        return result
