class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        if not rowIndex:
            return result
        for i in range(rowIndex):
            for j in range(len(result) - 1, 0, -1):
                result[j] = result[j] + result[j - 1]
            result.append(1)
        return result