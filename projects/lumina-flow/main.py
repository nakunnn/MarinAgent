def primes_up_to(n: int) -> list[int]:
    if n < 2: return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

if __name__ == '__main__':
    res = primes_up_to(50)
    print("Primes <= 50:", res)
    assert 47 in res
