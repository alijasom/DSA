class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        size=float('inf')
        sum=0
        i=0
        j=0
        while j<len(nums):
            sum=sum+nums[j]

            while sum >= target:
                size=min(size,j-i+1)
                sum = sum-nums[i]
                i+=1
            j+=1
        return 0 if size == float('inf') else size
        