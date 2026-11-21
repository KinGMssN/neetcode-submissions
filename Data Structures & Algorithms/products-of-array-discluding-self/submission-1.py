class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        z=0
        for j in nums:
            if j:
                p=p*j
            else:
                z+=1
        if z>1 : return [0]*len(nums)
        r=[0]*len(nums)
        for index, num in enumerate(nums):
            if z> 0:
                if num == 0:
                    r[index] = p
                else:
                    r[index] = 0
            else:
                r[index] = p // num
        return r

        