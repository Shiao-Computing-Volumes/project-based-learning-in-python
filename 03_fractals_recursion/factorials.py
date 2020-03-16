def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n-1)


def nonrecursive_factorial(n):
    if n == 1:
        return 1
    
    product = 1
    while (n > 0):
        product *= n
        n = n - 1
    return product
