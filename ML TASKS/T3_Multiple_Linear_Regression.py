import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 1. Dataset Setup (Simulating 50_Startups)
data = {
    'RD_Spend': [165349, 162597, 153441, 144372, 142107, 131876, 134615, 130298, 120542, 123334],
    'Admin_Spend': [136897, 151377, 101145, 118671, 91391, 99814, 147198, 145530, 148710, 121872],
    'Marketing_Spend': [471784, 443898, 407934, 383199, 366168, 362861, 127716, 323876, 311613, 303319],
    'State': ['New York', 'California', 'Florida', 'New York', 'Florida', 'New York', 'California', 'Florida', 'New York', 'California'],
    'Profit': [192261, 191792, 191050, 182901, 166187, 156991, 156122, 155752, 152211, 149760]
}
df = pd.DataFrame(data)

# 2. Heatmap Correlation Analysis
plt.figure(figsize=(6, 4))
sns.heatmap(df.select_dtypes(include=[np.number]).corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('T3: Feature Correlation Matrix')
plt.show()

# 3. Categorical Encoding (One-Hot Encoding for 'State')
df_encoded = pd.get_dummies(df, columns=['State'], drop_first=True)

# 4. Model Training
X = df_encoded.drop('Profit', axis=1)
y = df_encoded['Profit']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# 5. Adjusted R2 & Feature Coefficients
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
n, p = len(y_test), X_test.shape[1]
adj_r2 = 1 - ((1 - r2) * (n - 1) / (n - p - 1))

print("--- Coefficients ---")
for col, coef in zip(X.columns, model.coef_):
    print(f"{col}: {coef:.2f}")

print(f"\nR2 Score:          {r2:.4f}")
print(f"Adjusted R2 Score: {adj_r2:.4f}")
