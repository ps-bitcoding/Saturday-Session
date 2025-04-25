def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
        print(f"Multiplying {result} by {i}")

    return result


def main():
    number = 5
    print(f"Calculating factorial of {number}")

    fact = factorial(number)

    print(f"The factorial of {number} is {fact}")


if __name__ == "__main__":
    main()
