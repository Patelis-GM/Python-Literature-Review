import primes

if __name__ == "__main__":
    a = 2
    b = 100
    # Usage of the custom module
    result = primes.get_primes(a, b)
    print(f"Primes within [{a}, {b}] : {result}")
