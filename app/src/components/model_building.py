import os
import sys
import pickle
import pandas as pd

from sklearn.linear_model import LogisticRegression

from app.src.utils.exception import MyException
from app.src.utils.logger import logging
from app.src.constants import (ARTIFACT_DIR,
                               DATA_TRANSFORMATION_DIR_NAME,
                               DATA_TRANSFORMATION_TRAIN_FILE_NAME,
                               MODEL_TRAINER_DIR_NAME,
                               MODEL_TRAINER_TRAINED_MODEL_NAME,
                               MODEL_TRAINER_MAX_ITER,
                               MODEL_TRAINER_RANDOM_STATE)

class ModelBuilding:
    def __init__(self):
        try:
            self.train_file_path = os.path.join(ARTIFACT_DIR, DATA_TRANSFORMATION_DIR_NAME, DATA_TRANSFORMATION_TRAIN_FILE_NAME)
            self.model_path = os.path.join(ARTIFACT_DIR, MODEL_TRAINER_DIR_NAME, MODEL_TRAINER_TRAINED_MODEL_NAME)

        except Exception as e:
            raise MyException(e, sys)
        
    def load_data(self, file_path: str):
        try:
            df = pd.read_csv(file_path)
            logging.info("Data loaded successfully")
            return df

        except Exception as e:
            raise MyException(e, sys)

    def logistic_regression_model(self, x_train: pd.DataFrame, y_train: pd.DataFrame):
        try:
            logging.info("Creating Logistic Regression Model")
            model = LogisticRegression(max_iter = MODEL_TRAINER_MAX_ITER, random_state = MODEL_TRAINER_RANDOM_STATE)
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
            train_data = self.load_data(file_path = self.train_file_path)
            logging.info("Training Data loaded successfully")

            column_name = "placement_status"
            x_train = train_data.drop(columns = column_name)
            y_train = train_data[column_name]

            # Train on LogisticRegression Model
            model = self.logistic_regression_model(x_train = x_train, y_train = y_train)
            logging.info("Training complete")

            # Save model
            self.save_model(model = model, model_path = self.model_path)
            logging.info("Model saved successfully")
            logging.info("Model Building completed successfully.")

        except Exception as e:
            raise MyException(e, sys)
