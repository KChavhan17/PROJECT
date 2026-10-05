import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# 1. Load dataset
data = pd.read_csv("student_data.csv")

# 2. Input features and target
X = data[["study_hours", "attendance", "previous_marks"]]
y = data["result"]

# 3. Encode labels (Pass/Fail to numbers)
encoder = LabelEncoder()
y = encoder.fit_transform(y)

# 4. Split dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train Gaussian Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# 6. Check accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# 7. Save model and label encoder
with open("model.pkl", "wb") as file:
    pickle.dump((model, encoder), file)

print("Model saved successfully!")