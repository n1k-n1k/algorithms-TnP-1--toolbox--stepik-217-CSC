"""
Точки и отрезки

В первой строке задано два целых числа 1 ≤ n ≤ 50000 и 1 ≤ m ≤ 50000 —
количество отрезков и точек на прямой, соответственно.

Следующие n строк содержат по два целых числа ai и bi (ai ≤ bi)​— координаты концов отрезков.

Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8 по модулю.

Точка считается принадлежащей отрезку, если она находится внутри него или на границе.

Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.
"""

# testdada
# n, m = 6, 6
# segments = [[0, 31], [1, 3], [2, 3], [3, 4], [3, 5], [3, 6]]
# points = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


n, m = map(int, input().split())
segments = [list(map(int, input().split())) for _ in range(n)]
points = {int(i): 0 for i in input().split()}

starts = sorted(segments)
ends = sorted(segments, key=lambda x: x[1])

for p in points:
    start_cnt, end_cnt = 0, 0
    for s in starts:
        if s[0] <= p:
            start_cnt += 1

    for e in ends:
        if e[1] < p:
            end_cnt += 1

    points[p] = start_cnt - end_cnt

print(*points.values())
