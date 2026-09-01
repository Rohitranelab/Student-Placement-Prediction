import os
import sys
import json
import pickle
import pandas as pd

from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

from app.src.utils.logger import logging
from app.src.utils.exception import MyException

class ModelEvaluation:
    def load_data(self, file_path: str):
        try:
            logging.info("Data loaded successfully")
            return pd.read_csv(file_path)

        except Exception as e:
            raise MyException(e, sys)

    def load_model(self, model_path: str):
        try:
            with open(model_path, "rb") as file:
                model = pickle.load(file)
            logging.info("Model loaded successfully")
            return model

        except Exception as e:
            raise MyException(e, sys)

    def predict_model(self, model, x_test: pd.DataFrame, y_test: pd.DataFrame):
        try:
            logging.info("Predict model on test data")
            y_pred = model.predict(x_test)

            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)

            logging.info(f"Accuracy Score: {accuracy}")
            logging.info(f"Precision Score: {precision}")
            logging.info(f"Recall Score: {recall}")
            logging.info(f"F1 Score: {f1}")

            logging.info("Saved Model Performance")
            return {
                'Accuracy Score' : accuracy,
                'Precision Score' : precision,
                'Recall Score' : recall,
                'F1 Score' : f1
            }

        except Exception as e:
            raise MyException(e, sys)

    def save_model_performance(self, metrics, metrics_path: str):
        try:
            metrics_dir = os.path.dirname(metrics_path)
            if metrics_dir:
                os.makedirs(metrics_dir, exist_ok = True)

            with open(metrics_path, "w") as file:
                json.dump(metrics, file, indent = 4)
            logging.info(f"Model Performance Saved: {metrics_dir}")

        except Exception as e:
            raise MyException(e, sys)

    def main(self):
        try:
            logging.info("Model Evaluation Started.")

            # Load Data
            test_data = self.load_data(file_path = "./data/processed/test_processed.csv")
            logging.info("Data load successfully")

            column_name = "placement_status"
            x_test = test_data.drop(columns = column_name)
            y_test = test_data[column_name]

            # Load Model
            model = self.load_model(model_path = "./model/model.pkl")
            logging.info("Model Load successfully")

            # Model Predict
            metrics = self.predict_model(model = model, x_test = x_test, y_test = y_test)

            # Save metrics performance
            self.save_model_performance(metrics = metrics, metrics_path = "./reports/metrics/metric.json")
            logging.info("Model Performance saved")
            logging.info("Model Evaluation completed successfully.")

        except Exception as e:
            raise MyException(e, sys)

if __name__ == "__main__":
    obj = ModelEvaluation()
    obj.main()