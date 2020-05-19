"""
Двоичный поиск

В первой строке даны целое число 1 ≤ n ≤ 10^5 и массив A[1…n]
из n различных натуральных чисел, не превышающих 10^9, в порядке возрастания,
во второй — целое число 1 ≤ k ≤ 10^5 k натуральных чисел b1,…,bk, не превышающих 10^9.

Для каждого i от 1 до k необходимо вывести индекс 1 ≤ j ≤ n, для которого A[j]=bi,
или −1, если такого j нет.
"""


def bin_search(num, lst):
    if lst[-1] < num < lst[0]:
        return -1

    left, right = 1, len(lst)

    while left <= right:
        mid = (right + left) // 2

        if num < lst[mid - 1]:
            right = mid - 1
        elif num > lst[mid - 1]:
            left = mid + 1
        else:
            return mid

    return -1


n, *list_a = [int(i) for i in input().split()]
k, *list_b = [int(i) for i in input().split()]

print(*[bin_search(list_b[i], list_a) for i in range(k)])
