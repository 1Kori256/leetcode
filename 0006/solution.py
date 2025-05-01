class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ["" for _ in range(numRows)]
        direction = 0
        current_row = 0
        for c in s:
            rows[current_row] += c
            if direction == 0:
                current_row += 1
            else:
                current_row -= 1
            if current_row == numRows:
                current_row = max(current_row - 2, 0)
                direction = 1 - direction
            elif current_row == -1:
                current_row = min(numRows - 1, current_row + 2)
                direction = 1 - direction

        return "".join(rows)
