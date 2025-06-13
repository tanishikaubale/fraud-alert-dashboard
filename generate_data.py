from sklearn.datasets import make_classification
import pandas as pd

X, y = make_classification(
    n_samples=2000,
    n_features=4,
    n_informative=3,
    n_redundant=0,   # explicitly set to 0
    n_repeated=0,    # no repeated features
    random_state=42
)

df = pd.DataFrame(X, columns=["amount", "location", "transaction_type", "device_trust_score"])
df["is_fraud"] = y
df.to_csv("synthetic_transactions.csv", index=False)
print(" Synthetic data generated.")
