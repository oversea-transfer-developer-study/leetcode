class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        if length == 1:
            return 1

        prev = chars[0]
        res = prev
        count = 1

        for i in range(1, length):
            if chars[i] == prev:
                count += 1
            else:
                if count != 1:
                    res += str(count) + chars[i]
                    prev = chars[i]
                    count = 1
                else: 
                    res += chars[i]
                    prev = chars[i]
                    count = 1
        if count != 1:
            res += str(count)
        res = list(res)
        chars.clear()
        for i in range(0, len(res)):
            chars.append(res[i])
        return len(chars)