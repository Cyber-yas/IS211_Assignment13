
def fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def gcd(a, b):
    """Calculate the greatest common divisor of a and b using Euclid's algorithm."""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    """Recursively compare two strings."""
    if not s1 and not s2:  
        return 0
    elif not s1:  
        return -1
    elif not s2:  
        return 1
    elif s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:  
        return compareTo(s1[1:], s2[1:])


#Fibonacci function
print(f"fibonacci(5): {fibonacci(5)}")  
print(f"fibonacci(10): {fibonacci(10)}")  

# GCD function
print(f"gcd(48, 18): {gcd(48, 18)}")  
print(f"gcd(101, 103): {gcd(101, 103)}")  

#CompareTo function
print(f"compareTo('abc', 'abc'): {compareTo('abc', 'abc')}")  
print(f"compareTo('abc', 'abd'): {compareTo('abc', 'abd')}")  
print(f"compareTo('abd', 'abc'): {compareTo('abd', 'abc')}")  