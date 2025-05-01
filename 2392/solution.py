from typing import Self
from collections import defaultdict, deque
from dataclasses import dataclass, field


@dataclass
class Graph:
    # assumes verticies are labeled [1, ..., total_verticies]
    total_verticies: int
    graph: dict[int, set[int]] = field(default_factory=lambda: defaultdict(set))

    _order: deque = field(default_factory=lambda: deque())

    def add_edge(self: Self, u: int, v: int):
        self.graph[u].add(v)

    def _topological_sort_util(self: Self, v: int, visited: list[bool], resolving: set[int] | None = None) -> bool:
        if resolving is None:
            resolving = set()
        if v in resolving:
            return False
        resolving.add(v)
        for i in self.graph[v]:
            if not visited[i - 1]:
                status = self._topological_sort_util(i, visited, resolving)
                if not status:
                    return False

        visited[v - 1] = True
        self._order.appendleft(v)
        return True


    def topological_sort(self: Self) -> list[int] | None:
        visited = [False for _ in range(self.total_verticies)]

        for i in range(1, self.total_verticies + 1):
            if not visited[i - 1]:
                status = self._topological_sort_util(i, visited)
                if not status:
                    return None

        return list(self._order)


class Solution(object):
    def buildMatrix(self: Self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        """
        :type k: int
        :type rowConditions: List[List[int]]
        :type colConditions: List[List[int]]
        :rtype: List[List[int]]
        """

        row_order = self.sort_with_constraints(k, rowConditions)
        col_order = self.sort_with_constraints(k, colConditions)

        if row_order is None or col_order is None:
            return []

        return self.build_matrix(k, row_order, col_order)

    def sort_with_constraints(self: Self, k: int, constraints: list[list[int]]) -> list[int] | None:
        graph = Graph(k)

        for constraint in constraints:
            graph.add_edge(constraint[0], constraint[1])

        return graph.topological_sort()

    def build_matrix(self: Self, k: int, row_order: list[int], col_order: list[int]) -> list[list[int]]:
        matrix = [[0 for _ in range(k)] for _ in range(k)]
        col_indexes = [-1 for _ in range(k)]
        for i, num in enumerate(col_order):
            col_indexes[num - 1] = i

        for row_index, num in enumerate(row_order):
            col_index = col_indexes[num - 1]
            matrix[row_index][col_index] = num

        return matrix




print(Solution().buildMatrix(k=3, rowConditions=[[1,2],[3,2]], colConditions=[[2,1],[3,2]]))
print(Solution().buildMatrix(k=3, rowConditions=[[1,2],[2,3],[3,1],[2,3]], colConditions=[[2,1]]))

