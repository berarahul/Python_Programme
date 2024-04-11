myDict = {
    "fast": "In a Quick manner",
    "rahul": "A coder",
    "marks": [1,3,4,5,6,7,8,9,10,11],
    "anotherDict": {'rahul':'player'},
    1: 2
}

# Dictionary Methods
print(list(myDict.keys()))  # Prints the keys of the dictionary
print(myDict.values())  # Prints the values of the dictionary
print(myDict.items())  # Prints the (keys, values) for all content of the dictionary

print(myDict)
update_dictionary = {
    "arpan": "friend",
    "rahul": "A Cricketer"
}
myDict.update(update_dictionary)  # updates the dictionary by adding key-value pairs from updatedictonary
print(myDict) 

print(myDict.get("rahul")) # prints value associated with key "rahul"
print(myDict["rahul"]) # prints value associated with key "rahul"

#The Difference between
print(myDict.get("rahul2")) #Returns none as rahul2 is not present in the dictionary
print(myDict["rahul2"]) #Throws an error as rahul2 is not present in the Dictonary