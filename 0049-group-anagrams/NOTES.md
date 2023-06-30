```
​import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[(ord(c) - ord('a'))] += 1
            ans[tuple(count)].append(s)
        
        return ans.values()
```

1. Using a collections default dict to avoid any edge cases
2. Main datastructure used is a hashmap
3. First loop through all the elements in the string array
  - Create a count array of 26
  - Loop through the elements of the string
  - Find the position of the variable in the count array and increment it by one
    - `ord('c') - ord('a')` ==> 99 - 97 --> 2
    - `count = [0, 0, 1, 0, ...]`
4. Add this count array as a key to the hashmap with the string as the value
5. Return the hashmap values as the answer
