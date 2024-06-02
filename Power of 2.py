def sum_of_powers(n):
    powers = []
    power = 0
    while n > 0:
        if n % 2 == 1:
            powers.append(2 ** power)
        n //= 2
        power += 1
    return powers

# Taking input
n = int(input("Enter a number: "))

# Calculating and printing the result
result = sum_of_powers(n)
print("Numbers of power of 2 whose sum is equal to", n, ":", *result)
