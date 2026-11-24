class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        seen = {}
        res=0
        for j,c in enumerate(s):
            if c in seen and seen[c] >= i:
                i=seen[c]+1
            seen[c]=j
            res=max(res,j-i+1)
        return res            
            
            




        