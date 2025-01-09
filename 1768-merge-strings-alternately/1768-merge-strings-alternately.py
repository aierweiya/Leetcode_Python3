class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """將兩個字串交互穿插

        Args:
            str1: 第一個字串
            str2: 第二個字串

        Returns:
            一個新的字串，其中兩個字串的字符交互穿插
        """

        result = ""
        for i in range(min(len(word1), len(word2))):
            result += word1[i] + word2[i]
        # 如果其中一個字串較長，將剩餘的部分加到結果後面
        i += 1
        result += word1[i:] + word2[i:]
        return result
        