class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for c in range(0, len(candies)):
            if candies[c] + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
        