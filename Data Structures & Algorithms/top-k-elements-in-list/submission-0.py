class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for i in nums:
            c[i]=1+c.get(i,0)
        
        l=[]
        for i,j in c.items():
            l.append([j,i])
        l.sort()

        r=[]
        while len(r) < k:
            r.append(l.pop()[1])
        return r