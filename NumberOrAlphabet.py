ch = input("Enter a character : ")

if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    print(ch,'is an alphabet')

elif ch.isdigit():
    print(ch,'is a number, not an alphabet')

else:
    print(ch,'is not an alphabet')