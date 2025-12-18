n = int(input("Enter a number to find its prime factors: "))

factors = []
while n % 2 == 0:
    factors.append(2)
    n //= 2
i = 3
while i * i <= n:
    if n % i == 0:
        factors.append(i)
        n //= i
    else:
        i += 2
if n > 2:
    factors.append(n)

print("Prime factors:", factors)
