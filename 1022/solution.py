class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        cnt = 0
        req_depth = 1
        for row_i, row in enumerate(grid):
            for col_i, val in enumerate(row):
                if val == 1:
                    start = (row_i, col_i)
                elif val == 0:
                    req_depth += 1
        def walk_recursive(my_pos: tuple[int, int], depth = 0):
            nonlocal cnt
            if 0 > my_pos[0] or my_pos[0] >= len(grid):
                return
            elif 0 > my_pos[1] or my_pos[1] >= len(grid[0]):
                return
            current = grid[my_pos[0]][my_pos[1]]
            if current == -1:
                return
            elif current == 2:
                if depth == req_depth:
                    cnt += 1
                return
            
            grid[my_pos[0]][my_pos[1]] = -1
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_pos = (my_pos[0] + dir[0], my_pos[1] + dir[1])
                walk_recursive(new_pos, depth + 1)
            grid[my_pos[0]][my_pos[1]] = 0
    
        walk_recursive(start)
        return cnt