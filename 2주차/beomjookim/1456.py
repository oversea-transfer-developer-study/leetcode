class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        vowels = 'aeiou'
        temp_num = 0
        temp_s = [0] * len(s)

        for j in range(k):
            if s[j] in vowels:
                temp_num += 1
                temp_s[j] = 1

        res = temp_num

        while i < len(s)-k:
            if temp_s[i]: temp_num -= 1
            if s[i+k] in vowels:
                temp_num += 1
                temp_s[i+k] = 1

            if res < temp_num: res = temp_num

            i += 1

        return res
