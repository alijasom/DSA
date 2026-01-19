class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        window=set()
        curr_sum=0
        max_sum=0
        i=0
        for j in range(len(nums)):
            while nums[j] in window:
                window.remove(nums[i])
                curr_sum -= nums[i]
                i +=1
            window.add(nums[j])
            curr_sum += nums[j]

            if j-i+1 == k:
                max_sum = max(curr_sum,max_sum)
                window.remove(nums[i])
                curr_sum -=nums[i]
                i +=1
        return max_sum
                
        