from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# 1. Create a dummy dataset (100 samples, 4 features)
X, y = make_classification(n_samples=100, n_features=4, random_state=42)

# 2. Initialize a basic Logistic Regression model
model = LogisticRegression()

# 3. Train the model
model.fit(X, y)

# 4. Print success message
print("✨ scikit-learn is working perfectly inside VS Code!")
print(f"Model trained successfully! Coefficients: {model.coef_}")
