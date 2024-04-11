import pickle

data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Pickle the data and write it to a file
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
