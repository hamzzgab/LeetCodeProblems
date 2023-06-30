class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for val in s:            
            if val in ['(', '{', '[']:                
                stack.append(val)                
            else:
                if not stack:
                    return False
                curr = stack.pop()
                if curr == '(':
                    if val != ')':
                        
                        return False
                if curr == '[':
                    if val != ']':
                        return False
                if curr == '{':
                    if val != '}':
                        return False
        if len(stack) > 0:
            return False
        return True