def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def main():
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            factors = find_factors(num)
            print(f"The factors of {num} are: {factors}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
