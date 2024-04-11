def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    return (a * b) // calculate_gcd(a, b)

def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        gcd = calculate_gcd(num1, num2)
        lcm = calculate_lcm(num1, num2)

        print(f"GCD of {num1} and {num2} is: {gcd}")
        print(f"LCM of {num1} and {num2} is: {lcm}")

    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
