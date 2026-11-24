class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=j=0
        seen = defaultdict(int)
        res=0
        while j<len(s):
            while seen[s[j]]==1:
                seen[s[i]]-=1
                i+=1
            seen[s[j]]+=1
            res=max(res,j-i+1)
            j+=1
        return res            
            
            




        