from functools import cache

@cache
def fibo_cached(n):
    """
    en cachant les résultats on arrive
    à une complexité linéaire
    """
    if n <= 1:
        return n
    else:
        return fibo_cached(n-1) + fibo_cached(n-2)

"""
la suite de fibonacci
"""

def fibo(n):
    """
    # une implémentation naïve et inefficace
    """
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)