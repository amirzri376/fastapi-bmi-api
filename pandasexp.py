import random
import string
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

data = pd.read_csv("diabetes_dataset1.csv")
# print(data.shape)
print(data.columns)
# print(data.dtypes)
# print(data.head())
# print(data.describe())
# print(data.isnull().sum())
# print(data.duplicated().sum())
# print(data["Sex"].value_counts())
# print(data["Smoking_Status"].value_counts())
# data.plot.scatter(x="Age", y="HbA1c", title="Age vs HbA1c")
# plt.show()
data["High_Risk"] = data["HbA1c"] >= 6.5
print(data.columns)

X = data[
    [
        "Age",
        "Sex",
        "Cholesterol_Total",
        "Cholesterol_HDL",
        "GGT",
        "Serum_Urate",
        "Smoking_Status",
    ]
]
y = data["High_Risk"]

X_encoded = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Accuracy: {model.score(X_test, y_test):.2%}")

print(confusion_matrix(y_test, y_pred))

print(classification_report(y_test, y_pred))

for feature, coef in zip(X_encoded.columns, model.coef_[0]):
    print(f"{feature:30} → {coef:.4f}")
