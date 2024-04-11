powers_of_2 = lambda n: [2 ** i for i in range(n)]

# Input: Number of powers of 2 to display
n = 10  # Change this value to display a different number of powers

# Display the powers of 2
print("Powers of 2 up to 2^{}:".format(n - 1))
for i, power in enumerate(powers_of_2(n)):
    print(f"2^{i} = {power}")
