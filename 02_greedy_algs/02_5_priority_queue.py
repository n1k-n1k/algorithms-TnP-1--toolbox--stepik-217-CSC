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


def parse_input():
    q = PriorityQueueList()

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
