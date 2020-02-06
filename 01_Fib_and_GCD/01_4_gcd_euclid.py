'''
Наибольший общий делитель

По данным двум числам 1 <= a, b <= 2*10^9
найдите их наибольший общий делитель/
'''


def gcd(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a, b = a % b, b
        else:
            a, b = a, b % a

    if a == 0:
        return b
    elif b == 0:
        return a


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
