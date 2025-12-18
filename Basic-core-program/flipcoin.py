import random
n = input("Enter number of times to flip the coin: ")

if not n.isdigit() or int(n) <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    n = int(n)
    heads = 0
    tails = 0

   
    for _ in range(n):
        if random.random() < 0.5:
            tails += 1
        else:
            heads += 1

    
    heads_percentage = (heads / n) * 100
    tails_percentage = (tails / n) * 100

    
    print(f"Heads Percentage: {heads_percentage:}%")
    print(f"Tails Percentage: {tails_percentage:}%")
