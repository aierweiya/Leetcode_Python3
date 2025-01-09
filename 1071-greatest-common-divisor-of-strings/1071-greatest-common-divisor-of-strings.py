class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ''

        #gcd() 函數來計算最大公因數。
        length=gcd(len(str1), len(str2))
        return str1[:length]