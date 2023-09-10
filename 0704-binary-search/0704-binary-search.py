class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg, end = 0, len(nums) - 1
        
        while beg <= end:
            mid = (beg + (end - beg) // 2)
            
            if nums[mid] < target:
                beg = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:                
                return mid
        return -1