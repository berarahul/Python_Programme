# num = int(input("Enter the number"))
# for i in range(1,11):
#  print(f"{num}X{i}={num*i}") 


#  using while loop 
# Get user input for the number of rows and columns
num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of columns: "))

# Initialize the row counter
row = 1

# Outer loop for rows
while row <= num_rows:
    column = 1  # Reset the column for each new row
    
    # Inner loop for columns
    while column <= num_columns:
        result = row * column
        print(f"{row} x {column} = {result}\t", end="")
        column += 1
    
    print()  # Move to the next line for the next row
    row += 1
