class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r=len(nums)-1
        l=0
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        while l<=r:
            mid =(l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return -1
                
                    
                

        