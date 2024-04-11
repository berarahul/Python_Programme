def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        num += 6
    return True


num = int(input("Enter a number to check prime or not : "))
if is_prime(num):
    print(f"The number {num} is prime")
else:
    print(f"The number {num} is not prime")