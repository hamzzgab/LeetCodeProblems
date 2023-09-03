class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashS = {}
        hashT = {}
        
        if len(s) != len(t):
            return False
        
        for val in set(t):
            hashS[val] = s.count(val)
            hashT[val] = t.count(val)
        
        return hashS == hashT
