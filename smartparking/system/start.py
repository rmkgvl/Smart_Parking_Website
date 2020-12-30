import pickle
dict1 = {}
with open('filename.pickle', 'wb') as handle:
    pickle.dump(dict1, handle, protocol=pickle.HIGHEST_PROTOCOL)
