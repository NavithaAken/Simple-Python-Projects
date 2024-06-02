def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def find_lcm(numbers):
    lcm_result = numbers[0]
    for i in range(1, len(numbers)):
        lcm_result = lcm(lcm_result, numbers[i])
    return lcm_result

# Input
n = int(input())
numbers = list(map(int, input().split()))

# Output
print(find_lcm(numbers))
