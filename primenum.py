def prime(n):
    i = 0
    p = 0

    n = int(input("Enter any number: "))

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            p = 1
            break

    if p == 0:
        print(n, "is prime")
    else:
        print(n, "is composite")


n = 0
prime(n)