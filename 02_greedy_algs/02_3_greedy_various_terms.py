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
            prev = curr
            curr = prev + 1
            curr_max = 2 * (prev + 1)
            curr_last = n - sum_
            while curr < curr_max and curr < curr_last:
                curr += 1
            if curr < curr_last:
                curr = prev + 1
            lst.append(curr)
            sum_ += curr
        return lst


n = int(input())
lst = greedy_list(n)

print(len(lst))
print(*lst)
