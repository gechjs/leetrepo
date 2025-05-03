class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.s = SortedList()

    def seat(self) -> int:
        if not self.s:
            self.s.add(0)
            return 0
        
        d, res = self.s[0], 0
        for i in range(len(self.s) - 1):
            a, b = self.s[i], self.s[i+1]
            m = (b - a) // 2
            if m > d:
                d = m
                res = a + m
        
        if self.n - 1 - self.s[-1] > d:
            res = self.n - 1
        
        self.s.add(res)
        return res

    def leave(self, p: int) -> None:
        self.s.remove(p)
