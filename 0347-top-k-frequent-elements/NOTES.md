```
​class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            hash[num] = 1 + hash.get(num, 0)

        for v, c in hash.items():
            freq[c].append(v)
        
        res = []
        for num in range(len(freq) - 1, 0, -1):
            for n in freq[num]:
                res.append(n)
                if len(res) == k:
                    return res
```

1. Create a frequency the length of the nums array +1
2. Create a hash map with the count of the num in nums
3. Insert at index count the value n in the frequency
4. Iterate in the descending order
  - Append the sublist in the result
  - break when the result matches k
  - return the result
