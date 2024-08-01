def findGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

gcdResult = findGCD(36, 48)
print(gcdResult)  