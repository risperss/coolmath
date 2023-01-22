import math


def primes(bound: int) -> list[int]:
    numbers = list(range(2, bound + 1))
    limit = math.ceil(math.sqrt(bound))

    for i in range(limit):
        prime = numbers[i]

        if prime >= limit:
            break

        numbers = list(filter(lambda x: x % prime or x == prime, numbers))

    return numbers


def load_primes(bound: int) -> list[int]:
    result = []

    with open("primes1.txt") as file:
        for line in file:
            for prime in line.split():
                prime = int(prime)
                if prime > bound:
                    return result
                result.append(prime)

    return result


if __name__ == "__main__":
    file_primes = primes(1000)
    calc_primes = load_primes(1000)

    assert file_primes == calc_primes
