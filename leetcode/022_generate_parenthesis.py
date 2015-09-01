__author__ = 'Liang Li'
class Solution:
    # @param {integer} n
    # @return {string[]}

    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)

s = Solution()
print(s.generateParenthesis(3))