class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        total = 0

        if length == 1:
            if flowerbed[0] == 0:
                return n <= 1
        elif length == 2:
            if flowerbed[0] + flowerbed[1] == 0:
                return n <= 1
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            total += 1 

        for i in range(1,len(flowerbed)-1):
            prev = flowerbed[i-1]
            cur = flowerbed[i]
            nex = flowerbed[i+1]

            if prev == 0 and cur == 0 and nex == 0:
                total += 1
                flowerbed[i] = 1
    
        if flowerbed[length-1] == 0 and flowerbed[length-2] == 0:
            total += 1
        
        return total >= n

