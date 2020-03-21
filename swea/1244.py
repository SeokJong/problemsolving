class Solve:
    def __init__(self, inp):
        self.grid = inp
        self.result = set()
        self.cache = [[set() for _ in range(6)] for _ in range(16)]

    @staticmethod
    def transf(col, row):
        return (col * 4) + row

    @staticmethod
    def rev_transf(num):
        return num // 4, num % 4

    @staticmethod
    def move(col, row):
        res = []
        if col<3:
            res.append((col+1, row))
        if col>0:
            res.append((col-1, row))
        if row<3:
            res.append((col, row+1))
        if row>0:
            res.append((col, row-1))
        return res

    def count(self, pos, order, num):
        tp = self.transf(pos[0], pos[1])
        col, row = pos
        num += self.grid[col][row]
        if order == 6:
            self.result.add(num)
        else:
            if num in self.cache[tp][order]:
                return

            for next_pos in self.move(col, row):
                self.count(next_pos, order+1, num)

    def run(self):
        for i in range(16):
            self.count(self.rev_transf(i), 0, '')
        return len(self.result)


grid = [['1','1','1','1'], ['1','1','1','2'], ['1','1','2','1'], ['1','1','1','1']]
sol = Solve(grid)
test_case = 1
print(f'#{test_case} {sol.run()}')


