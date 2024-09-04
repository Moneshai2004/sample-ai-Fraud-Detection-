# model/train.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from smote import smote_oversample

# Load your preprocessed dataset
data = pd.read_csv('data/transactions.csv')
X = data.drop('is_fraud', axis=1)
y = data['is_fraud']

# Handle imbalance using SMOTE
X_resampled, y_resampled = smote_oversample(X, y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3)

# Model training
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'model/model.pkl')
