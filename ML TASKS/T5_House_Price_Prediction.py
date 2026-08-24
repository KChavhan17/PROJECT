import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# 1. Dataset Generation (2 numeric features with different scales)
np.random.seed(42)
X_raw = np.random.rand(100, 2) * [1000, 5]  # Feature 1: Sq.Ft (0-1000), Feature 2: Bedrooms (0-5)
y_gd = X_raw[:, 0] * 300 + X_raw[:, 1] * 10000 + 50000 + np.random.randn(100) * 5000

# 2. Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_raw)

# 3. Gradient Descent from Scratch
def gradient_descent(X, y, lr=0.01, iterations=500):
    m_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0
    cost_history = []

    for _ in range(iterations):
        y_pred = np.dot(X, weights) + bias
        cost = (1 / (2 * m_samples)) * np.sum((y_pred - y) ** 2)
        cost_history.append(cost)

        dw = (1 / m_samples) * np.dot(X.T, (y_pred - y))
        db = (1 / m_samples) * np.sum(y_pred - y)

        weights -= lr * dw
        bias -= lr * db

    return weights, bias, cost_history

# 4. Compare Learning Rates (0.01 vs 0.1)
w1, b1, cost1 = gradient_descent(X_scaled, y_gd, lr=0.01)
w2, b2, cost2 = gradient_descent(X_scaled, y_gd, lr=0.1)

plt.figure(figsize=(8, 4))
plt.plot(cost1, label='Learning Rate = 0.01')
plt.plot(cost2, label='Learning Rate = 0.1')
plt.xlabel('Iterations')
plt.ylabel('Cost (MSE)')
plt.title('Gradient Descent Convergence')
plt.legend()
plt.show()

# 5. Compare Gradient Descent with Scikit-Learn
model_sk = LinearRegression()
model_sk.fit(X_scaled, y_gd)

comp = pd.DataFrame({
    'Parameter': ['Weight 1 (Size)', 'Weight 2 (Beds)', 'Bias (Intercept)'],
    'GD (lr=0.1)': [w2[0], w2[1], b2],
    'Scikit-Learn': [model_sk.coef_[0], model_sk.coef_[1], model_sk.intercept_]
})

print("\n--- Parameter Comparison ---")
print(comp.to_string(index=False))
