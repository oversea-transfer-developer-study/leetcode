class Solution:
    def reverseVowels(self, s: str) -> str:
        # 한번의 iteration 안에 끝내는 좋은 방법이 있었다...
        # reverse니까 two pointer 활용하면 됨.
        # 그리고 s를 그대로 두고 진행하면 너무 느리니까, list로 바꿨다가 다시 바꿔서 리턴하기.

        vowels = "aeiouAEIOU"

        temp_s = list(s)

        i, j = 0, len(s)-1

        while True:
            while s[i] not in vowels and i < j: i += 1
            while s[j] not in vowels and j > i: j -= 1

            if i >= j: return "".join(temp_s)
            else:
                temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
                i, j = i+1, j-1
