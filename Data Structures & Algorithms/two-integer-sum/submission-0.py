class Solution:
    def twoSum(self, n: List[int], t: int) -> List[int]:
        c={}
        for i in range(len(n)):
            if (t-n[i]) in c:
                return [c[t-n[i]],i]
            c[n[i]]=i




        