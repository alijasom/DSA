class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=len(nums)-1
        k=0
        while k<=j:
            if nums[k]==1:
                k=k+1
            elif nums[k]==2:
                tmp=nums[j]
                nums[j]=nums[k]
                nums[k]=tmp

                j-=1
            else:
                tmp=nums[i]
                nums[i]=nums[k]
                nums[k]=tmp

                i+=1
                k+=1
        