class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        two_n = len(nums)
        nums.sort()
        sum = 0
        
        for i in range(0,two_n,2):
            sum += nums[i]
            
        return sum