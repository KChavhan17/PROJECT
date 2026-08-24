# 1. Dataset Generation (Years of Experience vs. Salary)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
X_t1 = np.array([1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7, 3.9, 4.0, 4.0, 4.1, 4.5])
y_t1 = np.array([39343, 46205, 37731, 43525, 39891, 56642, 60150, 54445, 64445, 57189, 63218, 55794, 56957, 57081, 61111])

# 2. Manual Least Squares Formula
x_mean = np.mean(X_t1)
y_mean = np.mean(y_t1)

m = np.sum((X_t1 - x_mean) * (y_t1 - y_mean)) / np.sum((X_t1 - x_mean) ** 2)
c = y_mean - (m * x_mean)

print(f"Calculated Slope (m): {m:.2f}")
print(f"Calculated Intercept (c): {c:.2f}")

# 3. Manual Predict Function
def predict_manual(x, slope, intercept):
    return slope * x + intercept

y_pred_t1 = predict_manual(X_t1, m, c)

# 4. Manual Metrics Calculation
mse_manual = np.mean((y_t1 - y_pred_t1) ** 2)
ss_total = np.sum((y_t1 - y_mean) ** 2)
ss_res = np.sum((y_t1 - y_pred_t1) ** 2)
r2_manual = 1 - (ss_res / ss_total)

print(f"Manual MSE: {mse_manual:.2f}")
print(f"Manual R2 Score: {r2_manual:.4f}")

# 5. Visualization
plt.figure(figsize=(8, 5))
plt.scatter(X_t1, y_t1, color='blue', label='Actual Data')
plt.plot(X_t1, y_pred_t1, color='red', linewidth=2, label='Manual Regression Line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary ($)')
plt.title('T1: Simple Linear Regression from Scratch')
plt.legend()
plt.show()
