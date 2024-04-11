def hello(x): # here create a function and recived  the copy of  value  of x
    x=45  # here change the value of x which is 45
    print(x) #and here print the copy value which value is 45
    return
x=13  #here initislize the variable name and put the value
hello(x) # here call the function and pass the copy of the value
print(x) # here print the actual value of x
    
   # This is  called passed by valu in python prprogram


    # Now i crrate the call by reference 

a=[1,2,3,4,5,6] #here I create a list
def hello2(x): # here create a function and pass the list via x arguments
    x[0]=12 # here change the index value which is 12 
    print(x) #here print the x 
    return
hello2(a)  # here call the function by reference
print(a)  # here updated list are printed which is same 