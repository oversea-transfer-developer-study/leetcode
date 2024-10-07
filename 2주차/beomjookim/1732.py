class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
            res = 0
            cur = 0

            for peak in gain:
                cur += peak
                if cur > res: res = cur

            return res
