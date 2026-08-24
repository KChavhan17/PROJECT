import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Dataset Setup
X_raw = np.array([1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7, 3.9, 4.0, 4.0, 4.1, 4.5])
y_raw = np.array([39343, 46205, 37731, 43525, 39891, 56642, 60150, 54445, 64445, 57189, 63218, 55794, 56957, 57081, 61111])

df = pd.DataFrame({'YearsExperience': X_raw, 'Salary': y_raw})

# 2. Exploratory Data Analysis (EDA)
print("--- T2: EDA Output ---")
print("Shape:", df.shape)
print("\nInfo:")
df.info()
print("\nDescription:\n", df.describe())
print("\nNull Values Check:\n", df.isnull().sum())

# 3. Train-Test Split (80% Train, 20% Test)
X = df[['YearsExperience']]
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate Performance
y_pred = model.predict(X_test)
print("\n--- Model Evaluation ---")
print(f"Coefficient: {model.coef_[0]:.2f}")
print(f"Intercept:   {model.intercept_:.2f}")
print(f"MAE:  {mean_absolute_error(y_test, y_pred):.2f}")
print(f"MSE:  {mean_squared_error(y_test, y_pred):.2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")
print(f"R2:   {r2_score(y_test, y_pred):.4f}")

# 6. Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].scatter(X_train, y_train, color='blue')
axes[0].plot(X_train, model.predict(X_train), color='red')
axes[0].set_title('Training Set: Actual vs Predicted')
axes[0].set_xlabel('Years Experience')
axes[0].set_ylabel('Salary')

axes[1].scatter(X_test, y_test, color='green')
axes[1].plot(X_train, model.predict(X_train), color='red')
axes[1].set_title('Test Set: Actual vs Predicted')
axes[1].set_xlabel('Years Experience')
axes[1].set_ylabel('Salary')

plt.tight_layout()
plt.show()
