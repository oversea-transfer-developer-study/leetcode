'''
input: list[int] - candies, integer - extra candy
output: list[bool] 

Clarifications
- there can be multiple kids having the same number of candies
- there will be at least 2 kids

Test Cases
[2,3,5,1,3], 3 => [true, true, true, false, true]
[1,1,1], 2 => [true, true, true]
[1,3,5], 1 => [false, false, true]

Approach 1) for each kid, add extraCandies and compare it to every other kid => O(N^2)
Approach 2) find the maximum number of candies any kid currently has and store the value.
            go through the list and check if the current candy + extra candy exceeds the max => O(N)

Plan
- define the function taking candies list and extraCandies integer as parameters
    - initialize max_candy to the maximum value in the list O(n)
    - initialize result list to the length of the inpu candies list
    - go through the each candy in the list 
        - if current candy + extra candy is greater than or equal to the max candy,
            - result[i] = True
    - return result list

TC: O(N), SC: O(N)
'''
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candy = max(candies)
        result = [False] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                result[i] = True
                
        return result