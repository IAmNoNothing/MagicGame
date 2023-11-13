from numba import njit


@njit("float64(float64, float64, float64)", fastmath=True)
def clamp(n, min_n, max_n):
    return max(min(max_n, n), min_n)
