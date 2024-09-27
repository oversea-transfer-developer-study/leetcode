class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # longest consecutive라는 점이 핵심이다. consecutive기 때문에 two pointer를 진행할 수 있는 것이다.
        # two-pointer 알고리즘을 생각해내도 디테일한 구현이 자꾸만 어긋난다.
        # 핵심은 가능하면 while이 아닌 for을 쓰는 것이다.
        # 아래의 코드는, l이 1일때는 바로잡지 않음으로 해서 최장을 유지하는 코드이다. 그러나 생각해내기 어렵다.

        # l=0
        
        # for r in range(len(nums)):
        #     if not nums[r]: k -= 1
        #     if k < 0:
        #         if not nums[l]: k += 1
        #         l += 1
        
        # return r-l+1

        # 따라서 좀 더 현실적인 코드는,

        l = 0
        res = 0

        for r in range(len(nums)):
            if not nums[r]:
                if k: k -= 1
                else:
                    while nums[l]: l += 1
                    l += 1
            if res < r+1-l: res = r+1-l
        
        return res
