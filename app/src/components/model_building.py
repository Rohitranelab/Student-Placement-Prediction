import os
import sys
import pickle
import pandas as pd

from sklearn.linear_model import LogisticRegression

from app.src.utils.exception import MyException
from app.src.utils.logger import logging

class ModelBuilding:
    def load_data(self, file_path: str):
        try:
            logging.info("Data loaded successfully")
            return pd.read_csv(file_path)

        except Exception as e:
            raise MyException(e, sys)

    def logistic_regression_model(self, x_train: pd.DataFrame, y_train: pd.DataFrame):
        try:
            logging.info("Creating Logistic Regression Model")
            model = LogisticRegression(max_iter = 2000, random_state = 42)
            model.fit(x_train, y_train)
            logging.info("Model training completed")
            return model

        except Exception as e:
            raise MyException(e, sys)

    def save_model(self, model, model_path):
        try:
            directory = os.path.dirname(model_path)
            if directory:
                os.makedirs(directory, exist_ok = True)

            with open(model_path, "wb") as file:
                pickle.dump(model, file)
            logging.info(f"Model saved to: {model_path}")

        except Exception as e:
            raise MyException(e, sys)

    def main(self):
        try:
            logging.info("Model Building started.")

            # Load Data
            train_data = self.load_data(file_path = "./data/processed/train_processed.csv")
            logging.info("Data loaded successfully")

            column_name = "placement_status"
            x_train = train_data.drop(columns = column_name)
            y_train = train_data[column_name]

            # Train on LogisticRegression Model
            model = self.logistic_regression_model(x_train = x_train, y_train = y_train)
            logging.info("Training complete")

            # Save model
            self.save_model(model = model, model_path = "./model/model.pkl")
            logging.info("Model saved successfully")
            logging.info("Model Building completed successfully.")

        except Exception as e:
            raise MyException(e, sys)

if __name__ == "__main__":
    obj = ModelBuilding()
    obj.main()
