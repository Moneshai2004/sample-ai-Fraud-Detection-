# model/smote.py
from imblearn.over_sampling import SMOTE

def smote_oversample(X, y):
    sm = SMOTE(random_state=42)
    X_res, y_res = sm.fit_resample(X, y)
    return X_res, y_res
