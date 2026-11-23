class Solution:
    def maxProfit(self, p: List[int]) -> int:
        i=j=0
        m=0
        while(j<len(p)):
            lm=p[j]-p[i]
            m=max(m,lm)
            if lm>=0:
                j+=1
            else:
                i=j
                j+=1
        return m
            

        