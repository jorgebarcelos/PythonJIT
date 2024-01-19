from numba import njit


@njit
def loop(k):
    for i in range(0, 1000):
        for j in range(0, 1000):
            print(f'i = {i} | j = {j}')
            k += 1
    print(k)


loop = loop(0)