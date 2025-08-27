import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the newly created Training.csv
df = pd.read_csv('data/Training.csv')
X = df.drop('Disease', axis=1)
y = df['Disease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

print('Model Accuracy:', model.score(X_test, y_test))
joblib.dump(model, 'disease_model.pkl')
joblib.dump(list(X.columns), 'symptom_columns.pkl')