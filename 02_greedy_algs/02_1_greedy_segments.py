'''
Покрыть отрезки точками

По данным nn отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1 <= n <= 100 отрезков.
Каждая из последующих nn строк содержит по два числа
0 <= l <= r <= 10^9, задающих начало и конец отрезка.

Выведите оптимальное число m точек и сами m точек.
Если таких множеств точек несколько, выведите любое из них.


!!!
Если не получается разобраться с условием задачи,
то попробуйте представить эту задачу так:

есть несколько дощечек разной длины (это наши отрезки n).
Нужно прибить их к полу так, чтобы если комната перевернулась они не попадали.
Вот минимальное количество гвоздей в этой задаче и точки куда они прибиты
и будет решением.
'''

# v2. рефакторинг: оптимизация сложности алгоритма

n = int(input())
segs = [list(map(int, input().split())) for i in range(n)]
segs.sort(key=lambda seg: seg[1])
dots = [segs[0][1]]

for start, stop in segs[1:]:
    if start > dots[-1]:
        dots.append(stop)

print(len(dots))
print(*dots, sep=' ')