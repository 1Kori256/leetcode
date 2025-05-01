class Solution(object):
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        result = set()
        for i in range(0, n):
            x = self.generateParenthesis(i)
            y = self.generateParenthesis(n - i - 1)
            for a in x:
                for b in y:
                    result.add(a + b + "()")
                    result.add(a + "()" + b)
                    result.add("()" + a + b)
                    result.add("(" + a + b + ")")
                    result.add("(" + a + ")" + b)
                    result.add(a + "(" + b + ")")

        return list(result)
        