class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0

        while j < len(chars):
            target = chars[j]
            cnt = 0
            while j < len(chars) and chars[j] == target:
                j += 1
                cnt += 1
            chars[i] = target
            i += 1
            if cnt > 1:
                for c in str(cnt):
                    chars[i] = c
                    i += 1
        
        return i
        
