class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        c={}
        for i,j in enumerate(n):
            d=t-j
            if d in c:
                return [c[d],i]
            c[j]=i




        