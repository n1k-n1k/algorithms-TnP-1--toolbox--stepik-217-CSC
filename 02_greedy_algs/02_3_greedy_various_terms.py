'''
Различные слагаемые

По данному числу 1 <= n <= 10^9 найдите максимальное число k,
для которого n можно представить как сумму k различных натуральных слагаемых.
Выведите в первой строке число k, во второй — k слагаемых.
'''


def greedy_list(n):
    if n == 1 or n == 2:
        return [n]
    else:
        lst = [1]
        curr = 1
        sum_ = 1
        while sum_ < n:
            curr += 1
            sum_ += curr
            lst.append(curr)
        if sum_ > n:
            lst.pop()
            prev = lst.pop()
            lst.append(n - sum_ + prev + curr)
        return lst


n = int(input())
lst = greedy_list(n)

print(len(lst))
print(*lst)
