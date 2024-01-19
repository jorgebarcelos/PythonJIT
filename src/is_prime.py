from numba import njit


@njit
def is_prime(n):
    '''JIT speed test N² complexity algorithm '''
    for i in range(2, n):
        if n % i == 0:
            return False
        return True
    
primes = []


for i in range(2, 250001):
    if is_prime(i):
        primes.append(i)


print(len(primes))



# JIT result: 0.66s user 0.53s system 272% cpu 0.440 total
# NO JIT result: 0.06s user 0.00s system 99% cpu 0.061 total