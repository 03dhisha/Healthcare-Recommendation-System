import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load symptom-disease training dataset
df = pd.read_csv('data/symtoms_df.csv')

# Separate features and target
X = df.drop(['prognosis'], axis=1)
y = df['prognosis']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'disease_model.pkl')

print("✅ Model trained and saved as disease_model.pkl")
