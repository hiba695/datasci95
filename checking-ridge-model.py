import pickle

with open("models/ridge1.pkl", "rb") as f:
    ridge_model = pickle.load(f)

print(type(ridge_model))   # e.g. <class 'sklearn.linear_model._ridge.Ridge'>
print(ridge_model)         # shows the model and parameters
print("Features expected:", ridge_model.n_features_in_)

