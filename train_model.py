import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load dataset
df = pd.read_csv("insurance.csv")

# convert male/female into numbers
# male = 1
# female = 0

df['sex'] = df['sex'].map({
    'male':1,
    'female':0
})

# input features
X = df[['age', 'children', 'charges', 'sex']]

# target variable
y = df['bmi']

# split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model
model = LinearRegression()

# train
model.fit(X_train, y_train)

# save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model Saved Successfully")