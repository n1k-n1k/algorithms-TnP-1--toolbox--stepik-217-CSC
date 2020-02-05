'''
Небольшое число Фибоначчи

Дано целое число 1 <= n <= 40, необходимо вычислить n-е число Фибоначчи
(напомним, что F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) при n >= 2).
'''


# итерационное решение
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        f_2, f_1 = 0, 1
        for i in range(n - 1):
            f_2, f_1 = f_1, f_2 + f_1
    return f_1


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
