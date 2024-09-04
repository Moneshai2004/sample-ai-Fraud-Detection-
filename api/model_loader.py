# api/model_loader.py
import joblib

class ModelLoader:
    def __init__(self, model_path='model/model.pkl'):
        self.model = joblib.load(model_path)

    def predict(self, data):
        # Assuming `data` is a preprocessed DataFrame ready for prediction
        prediction = self.model.predict(data)
        return prediction

# Example usage:
# loader = ModelLoader()
# prediction = loader.predict(preprocessed_data)
