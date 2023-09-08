class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = max(min(height[l], height[r]) * (r - l), area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return area