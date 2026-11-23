class Solution:
    def trap(self, h: List[int]) -> int:
        lm=rm=t=0
        l=0
        r=len(h)-1
        while (l<r):
            if (h[l]<=h[r]):
                if(lm>h[l]):
                    t+=lm-h[l]
                else:
                    lm=h[l]
                l+=1
            else:
                if rm >h[r]:
                    t+=rm-h[r]
                else:
                    rm=h[r]
                r-=1
        return t