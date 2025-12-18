n = int(input("Enter the value of N (N != 0): "))

if n <= 0:
    print("Invalid input. Enter a positive integer.")
else:
    harmonic = 0.0
    i = 1
    while i <= n:
        harmonic += 1 / i
        i += 1
    print(f"The {n}th Harmonic number is: {harmonic:.4f}")
