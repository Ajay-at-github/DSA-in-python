class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(n, leftCount, rightCount, output, result):
            if leftCount >= n and rightCount >= n:
                outputStr = "".join(output)
                result.append(outputStr)

            if leftCount < n:
                output.append("(")
                backtrack(n, leftCount + 1, rightCount, output, result)
                output.pop()

            if rightCount < leftCount:
                output.append(")")
                backtrack(n, leftCount, rightCount + 1, output, result)
                output.pop()

        result = []
        output = []
        backtrack(n, 0, 0, output, result)
        return result



