'''
input: list- flowerbed(0: empty, 1: flower), integer n: # of new flowers
output: boolean - return true if n new flowers can be planted in the flowerbed

Clarifications
- flowers can't be planted next to each otehr
- n can be zero
- can we modify the input list during the process? yes

Test cases
[1,0,0,0,1], 1 => True  [1,0,1,0,1]
[1,1,1],1 => False
[0,0,0,0],2 => True  [1,0,1,0]
[0], 1 => True [1]

Appraoch 1) check all the possibilities o(n^2)
Approach 2) single pass. for each empty spot, check the left and right neighbors O(N)

Plan
- define the function taking flowerbed list and integer as parameters
    - hanlde edge case: if n is equal to 0, return True
    - go through each spot
        - if the current spot is empty, check if the previous and next spots are also empty or out of bounds
            - plant a flower, reduce n by 1
            - if n reaches 0, return True
    - return n == 0

TC: O(N), SC: O(1)
'''
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
            
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True
        return n == 0