class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg, end, pos = 0, len(nums) - 1, -1
        
        while beg <= end:
            mid = (beg + end) // 2
            
            if nums[mid] == target:
                pos = mid
                return pos
            elif nums[mid] < target:
                beg = mid + 1
            elif nums[mid] > target:
                end = mid - 1
        return pos