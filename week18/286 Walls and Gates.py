class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return rooms

        rows = len(rooms)
        cols = len(rooms[0])
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque()

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:          #Adding gates
                    queue.append((row, col))

        while queue:
            curr_row, curr_col = queue.popleft()
            for i in neighbors:
                r = curr_row + i[0]
                c = curr_col + i[1]
                if 0 <= r < rows and 0 <= c < cols and (rooms[r][c] > rooms[curr_row][curr_col]):
                    rooms[r][c] = rooms[curr_row][curr_col] + 1
                    queue.append((r, c))

"""bfs traversal 0(mn) complexity"""
