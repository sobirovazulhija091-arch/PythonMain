def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True
print(is_prime(16))

def count_prime(m):
    count = 0
    for i in range(2, m+1):
        if is_prime(i):
            count += 1
    return count         
print(count_prime(16))
