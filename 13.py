num = int(input("Enter a number: "))
factors = [i for i in range(1, num + 1) if num % i == 0]
print(f"Factors of {num}: {', '.join(str(i) for i in factors)}")