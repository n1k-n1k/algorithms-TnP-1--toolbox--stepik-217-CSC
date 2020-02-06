'''
Наибольший общий делитель

По данным двум числам 1 <= a, b <= 2*10^9
найдите их наибольший общий делитель/
'''


def gcd(a, b):
    while a and b:
        if a >= b:
            a %= b
        else:
            b %= a

    return max(a, b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
