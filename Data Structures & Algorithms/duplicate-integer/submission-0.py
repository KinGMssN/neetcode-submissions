class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=[]
        for i in nums:
            if i not in l:
                l.append(int(i))
                continue
            return True
        return False 
        