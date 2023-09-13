class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(a + b)
            elif t == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif t == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(a * b)
            elif t == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(t))

        return stack[0]