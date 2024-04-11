def sumNatural(num: int) -> int:
    return num* (num + 1) // 2
num=int(input("Enter a Number"))
print(f"Sum of 1 to{num} is {sumNatural(num)}")