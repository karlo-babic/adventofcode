class Room:
    def __init__(self, filepath):
        with open(filepath) as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
        self.height = len(lines)
        self.width = len(lines[0])
        self.grid = []
        for y in range(0, self.height):
            if len(lines[y]) == 0: continue
            self.grid.append(list(lines[y]))
            print(self.grid[y])
        self.kernel = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def _num_neighbors(self, y, x):
        count = 0
        for d in self.kernel:
            if y+d[0] < 0 or y+d[0] >= self.height or x+d[1] < 0 or x+d[1] >= self.width:
                continue
            if self.grid[y+d[0]][x+d[1]] == '@':
                count += 1
        return count

    def count(self):
        total_count = 0
        for y in range(0, self.height):
            for x in range(0, self.width):
                if self.grid[y][x] != '@':
                    continue
                if self._num_neighbors(y, x) < 4:
                    total_count += 1
        return total_count


room = Room('4_input.txt')
print(room.count())