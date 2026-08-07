import pickle
import os

pickle_file = os.path.join('data', 'model.pkl')
with open(pickle_file, 'rb') as f:
    model = pickle.load(f)

print("Model type:", type(model))
print("\nFeatures model expects:")
print(model.feature_names_in_)