class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        return sum([(len(chunk)-1)//2 for chunk in "".join(map(str, [0] + flowerbed + [0])).split("1") if chunk]) >= n
