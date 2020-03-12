'''
Очередь с приоритетами

Первая строка входа содержит число операций 1 ≤ n ≤ 10^5.
Каждая из последующих n строк задают операцию одного из следующих двух типов:

Insert x, где 0 ≤ x ≤ 10^9 - целое число;
ExtractMax.

Первая операция добавляет число x в очередь с приоритетами,
вторая — извлекает максимальное число и выводит его.
'''


class PriorityQueueList:
    def __init__(self, lst=None):
        self.lst = lst or []

    def __str__(self):
        return f'{self.lst}'

    def get_max(self):
        return self.lst[-1]

    def extract_max(self):
        if len(self.lst):
            return self.lst.pop()

    def insert(self, n):
        self.lst.append(n)
        self.lst.sort()


class PriorityQueueHeap:
    def __init__(self, heap=None):
        self._heap = heap or []

    @staticmethod
    def _parent_i(i):
        if i:
            return (i - 1) // 2

    def _left_i(self, i):
        _left = i * 2 + 1
        if _left <= len(self._heap) - 1:
            return _left

    def _right_i(self, i):
        _right = i * 2 + 2
        if _right <= len(self._heap) - 1:
            return _right

    def _min_child_i(self, i):
        _right_ind = self._right_i(i)
        _left_ind = self._left_i(i)
        _right = self._heap(_right_ind)
        _left = self._heap(_left_ind)

        if not (_right and _left):
            return None
        if not _right or _right > _left:
            return _left_ind
        else:
            return _right_ind

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _move_up(self, i):
        while i > 0:
            if self._heap[i] < self._heap[self._parent_i(i)]:
                self._swap(i, self._parent_i(i))
                i = self._parent_i(i)
            else:
                return

    def _move_down(self, i):
        while self._min_child_i(i):
            tmp = i
            min_child_tmp = self._min_child_i(tmp)
            self._swap(tmp, min_child_tmp)
            i = min_child_tmp

    def get_max(self):
        return self._heap[-1]

    def extract_max(self):
        if len(self._heap):
            return self._heap.pop()

    def get_min(self):
        return self._heap[0]

    def extract_min(self):
        if len(self._heap):
            root = self._heap[0]
            self._heap[0] = self._heap.pop()
            self._move_down(0)
            return root

    def insert(self, n):
        self._heap.append(n)
        self._move_up(len(self._heap) - 1)


def parse_input():
    q = PriorityQueueHeap()

    for _ in range(int(input())):
        cmd = input()
        if cmd == 'ExtractMax':
            max_ = q.extract_max()
            print(max_)
        else:
            n = int(cmd.split()[1])
            q.insert(n)


if __name__ == '__main__':
    parse_input()
