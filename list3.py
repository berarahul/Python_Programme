marks = [3,5,6,"Rahul",True]

print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

if "6" in marks:
    print("Yes")
else:
    print("No")

    if "ahul" in "Rahul":
        print("Yes") 
        print(marks[0:3])
        print(marks[:])
        print(marks[0:4:1])

        lst=[i*i for i in range(4) if i %2==0]
        print(lst)