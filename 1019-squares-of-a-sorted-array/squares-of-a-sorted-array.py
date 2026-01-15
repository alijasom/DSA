class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        i=0
        j=n-1
        k=n-1
        while i<=j:
            if abs(nums[i])> abs(nums[j]):
                res[k]=nums[i]**2
                i +=1
            else:
                res[k]=nums[j]**2
                j -=1
            k -=1
        return res


        