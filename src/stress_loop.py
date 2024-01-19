import time
from numba import njit

@njit
def tax_value(qtd):
    for i in range(qtd):
        new_value = qtd * 1.1


init_time = time.time()
tax_value(1000000000)
end_time = time.time()

print(end_time - init_time)