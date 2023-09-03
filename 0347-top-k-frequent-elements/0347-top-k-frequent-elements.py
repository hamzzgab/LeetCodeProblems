class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = [[] for _ in range(len(nums)+1)]
        
        hash = {}
        
        for num in nums:
            hash[num] = 1 + hash.get(num, 0)
            
        for num, count in hash.items():
            freq[count].append(num)
    
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res