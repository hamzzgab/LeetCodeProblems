class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ans = "".join([n for n in s if n.isalnum()]).lower()
        return ans == ans[::-1]