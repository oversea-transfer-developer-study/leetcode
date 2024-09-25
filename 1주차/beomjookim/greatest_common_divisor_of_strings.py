class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # 1 첫 글자부터 되는지 확인
        # 이 경우 각 케이스마다 m*n의 시간이 걸림.
        # 최악의 경우 m*m*n

        # 2 우선 앞에서부터 공통인 가장 긴 글 찾기.
        # 케이스마다 m*n 걸림.
        # 최악의 경우 m*m*n

        # 두 케이스 모두 최악의 경우의 Time Complexity는 동일하지만, 디테일로 들어가면
        # 2가 더 적게 걸릴 것으로 추정.

        ###  gcd를 구하는 유용한 방식, 기억하자.
        # def gcd(a:int,b:int)->int:
        #     while b:
        #         a,b=b,a%b
        #     return a

        def len_check(l1, l2, cand_length): return not (l1 % cand_length or l2 % cand_length)
        def cd_check(str1, str2, temp): return str1 == temp * (l1//len(temp)) and str2 == temp * (l2//len(temp))

        i = 0
        cand = ""

        l1, l2 = len(str1), len(str2)

        while str1[i] == str2[i]:
            cand += str1[i]
            i += 1

            if i == l1 or i == l2: break

        if not cand: return ""

        while True:
            temp = cand

            if not cand: return ""

            if not len_check(l1, l2, len(cand)):
                if cand: cand = cand[:-1]
                else: return ""
            
            if cd_check(str1, str2, cand): return cand
            else: cand = cand[:-1]
