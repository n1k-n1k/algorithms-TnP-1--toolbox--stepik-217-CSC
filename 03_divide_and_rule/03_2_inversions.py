"""
Число инверсий

Первая строка содержит число 1 ≤ n ≤ 10^5 , вторая — массив A[1…n], содержащий натуральные числа,
не превосходящие 10^9.

Необходимо посчитать число пар индексов 1 ≤ i < j ≤ n, для которых A[i] > A[j].
(Такая пара элементов называется инверсией массива.
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
например, в упорядоченном по неубыванию массиве инверсий нет вообще, а в массиве,
упорядоченном по убыванию, инверсию образуют каждые два элемента.)
"""


def merge_sort(lst):
    if len(lst) < 2:
        return lst[:]

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    return merge_inv(left, right)


def merge_inv(left, right):
    global inv_cnt

    merged = []
    i, j = 0, 0
    len_left, len_right = len(left), len(right)

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_cnt += len_left - i  # остаток левой части - инверсии

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


if __name__ == '__main__':
    _, array = input(), [int(i) for i in input().split()]

    inv_cnt = 0
    merge_sort(array)
    print(inv_cnt)
