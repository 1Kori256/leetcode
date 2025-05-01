class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for j in range(n // 2):
            for i in range(j, n - j - 1):
                my_points = [(j, i), (i, n - j - 1), (n - j - 1, n - i - 1), (n - i - 1, j)]
                vals = []
                for p in [my_points[-1]] + my_points[:-1]:
                    vals.append(matrix[p[0]][p[1]])
                for p, v in zip(my_points, vals):
                    matrix[p[0]][p[1]] = v


