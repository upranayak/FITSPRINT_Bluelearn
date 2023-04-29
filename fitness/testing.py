import pickle

# load the vectorizer and model
with open("count.pkl", "rb") as f:
    vectorizer = pickle.load(f)
    
with open("classifier_depression.pkl", "rb") as f:
    model = pickle.load(f)

# define a function to make predictions
def predict(text):
    # create a 2D array with shape (1, n)
    vectorized_text = vectorizer.transform([text])
    dense_vectorized_text = vectorized_text.toarray()
    # make the prediction
    prediction = model.predict(dense_vectorized_text)
    print(len(prediction))
    return prediction[0]

# test the function
text = "I am very happy today"
prediction = predict(text)
print(prediction)