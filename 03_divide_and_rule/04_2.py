"""
Точки и отрезки

В первой строке задано два целых числа 1 ≤ n ≤ 50000 и 1 ≤ m ≤ 50000 —
количество отрезков и точек на прямой, соответственно.

Следующие n строк содержат по два целых числа ai и bi (ai ≤ bi)​— координаты концов отрезков.

Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю.

Точка считается принадлежащей отрезку, если она находится внутри него или на границе.

Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""

from random import randint


def quick_sort_mod(lst, start, end):
    while start < end:
        i = pivot(lst, start, end)
        lst[start], lst[i] = lst[i], lst[start]

        j = partition_mod(lst, start, end)
        quick_sort_mod(lst, start, j - 1)
        # quick_sort_mod(lst, j + 1, end)
        start = j + 1


def partition_mod(lst, start, end):
    piv = lst[start]
    i = start + 1
    for j in range(start + 1, end):
        if lst[j] < piv:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[start], lst[i - 1] = lst[i - 1], lst[start]
    return i - 1


def pivot(lst, start, end):
    # return start
    return randint(start, end - 1)


# testdada
# n, m = 6, 6
# starts = [0, 1, 2, 3, 3, 3]
# ends = [31, 3, 3, 4, 5, 6]
# points = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
# result = '2 3 6 4 3 2'

n, m = map(int, input().split())
starts = []
ends = []

for _ in range(n):
    s, e = map(int, input().split())
    starts.append(s)
    ends.append(e)

points = {int(i): 0 for i in input().split()}

quick_sort_mod(starts, 0, n)
quick_sort_mod(ends, 0, n)

for p in points:
    start_cnt, end_cnt = 0, 0
    for s in starts:
        if s <= p:
            start_cnt += 1
        else:
            break

    for e in ends:
        if e < p:
            end_cnt += 1
        else:
            break

    points[p] = start_cnt - end_cnt

print(*points.values())
