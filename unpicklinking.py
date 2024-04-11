import pickle

# Unpickle the data from the file
with open('data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

print(loaded_data)
