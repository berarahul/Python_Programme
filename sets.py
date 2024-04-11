a={1,3,4,5,1}
print(type(a))
print(a)
#set is a collection of not repetable elements

# Important: This syntax will create an empty dictonary and not an empty set

b={}
print(type(b))

# An Empty set can be created using the below Syntax:
c= set()
print(type(c))
c.add(4)
c.add(5)   # ADDING A VALUE REPEATEDLY DOES NOT CHANGES A SET.
c.add(4)
c.add(5)
c.add(3)
c.add(2)
# c.add([4,5,6])  #TypeError: unhashable type: 'list' # cannot add list
c.add((1,3,4,5)) # yes we can add the tuple in set
# c.add({4:5})  # cannot add list or Dictonary in set
print(c)

#length of the set
print(len(c)) #prints the length of a set

#Removel of an Item
c.remove(5) #removes 5 from set b
# c.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(c)


print(c.pop())

s1={1,2,3,4,}
s2={1,3,4,5,7,8,9,}
print(s1.union(s2))
print(s1.intersection(s2))