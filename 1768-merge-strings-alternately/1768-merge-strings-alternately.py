class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(min(len(word1), len(word2))):
            result += word1[i] + word2[i]
        # 如果其中一個字串較長，將剩餘的部分加到結果後面
        i += 1
        result += word1[i:] + word2[i:]
        return result
        