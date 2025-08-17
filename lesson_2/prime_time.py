from time import perf_counter
from functools import lru_cache

@lru_cache
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

    return True

start_time1 = perf_counter()
is_prime(73729261)
end_time1 = perf_counter()
print(f"{end_time1 - start_time1} seconds.")
# 2.0238720000052126 seconds.

start_time2 = perf_counter()
is_prime(73729261)
end_time2 = perf_counter()
print(f"{end_time2 - start_time2} seconds.")
# 2.0238720000052126 seconds.