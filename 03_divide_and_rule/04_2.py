"""
Точки и отрезки

В первой строке задано два целых числа 1 ≤ n ≤ 50000 и 1 ≤ m ≤ 50000 —
количество отрезков и точек на прямой, соответственно.

Следующие n строк содержат по два целых числа ai и bi (ai ≤ bi)​— координаты концов отрезков.

Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю.

Точка считается принадлежащей отрезку, если она находится внутри него или на границе.

Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""


def quick_sort_mod(lst, start, end):
    if end - start > 1:
        pivot = partition(lst, start, end)
        quick_sort_mod(lst, start, pivot)
        quick_sort_mod(lst, pivot + 1, end)
    return lst


def partition(lst, start, end):
    pivot = lst[start]
    i = start + 1
    j = end - 1

    while True:
        while i <= j and lst[i] <= pivot:
            i = i + 1
        while i <= j and lst[j] >= pivot:
            j = j - 1

        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
        else:
            lst[start], lst[j] = lst[j], lst[start]
            return j


# testdada
# n, m = 6, 6
# starts = [0, 1, 2, 3, 3, 3]
# stops = [31, 3, 3, 4, 5, 6]
# points = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


n, m = map(int, input().split())

starts = []
stops = []

for _ in range(n):
    a, b = map(int, input().split())
    starts.append(a)
    stops.append(b)

points = {int(i): 0 for i in input().split()}

starts = quick_sort_mod(starts, 0, n)
ends = quick_sort_mod(stops, 0, n)

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
