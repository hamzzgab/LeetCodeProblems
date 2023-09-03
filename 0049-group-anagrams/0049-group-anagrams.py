import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hash = collections.defaultdict(list)
        
        for str in strs:
            count = [0]*26
            for s in str:
                count[ord(s)-ord('a')] += 1
            
            hash[tuple(count)].append(str)
            
        return hash.values()