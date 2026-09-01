import os
import sys
import pandas as pd

from app.src.utils.exception import MyException
from app.src.utils.logger import logging

class DataTransformation:
    def load_data(self, file_path: str):
        try:
            logging.info("Data loaded successfully")
            return pd.read_csv(file_path)

        except Exception as e:
            raise MyException(e, sys)

    def save_data(self, train_data: pd.DataFrame, test_data: pd.DataFrame, data_path: str):
        try:
            raw_data = os.path.join(data_path, "processed")
            os.makedirs(raw_data, exist_ok = True)

            train_path = os.path.join(raw_data, "train_processed.csv")
            test_path = os.path.join(raw_data, "test_processed.csv")

            train_data.to_csv(train_path, index = False)
            test_data.to_csv(test_path, index = False)

            logging.info(f"Training data saved to: {train_path}")
            logging.info(f"Testing data saved to: {test_path}")

        except Exception as e:
            raise MyException(e, sys)

    def main(self):
        try:
            logging.info("Data Transformation started.")

            # Load Training and Testing Data
            train_data = self.load_data(file_path = "./data/raw/train.csv")
            test_data = self.load_data(file_path = "./data/raw/test.csv")
            logging.info("Training and Testing data loaded successfully")

            # Checking target column are present or not in training and testing data
            target_column = "placement_status"

            if target_column not in train_data.columns:
                logging.info(f"{target_column} are not present in training data")

            if target_column not in test_data.columns:
                logging.info(f"{target_column} are not present in testing data")

            # Saving processed data
            self.save_data(train_data = train_data, test_data = test_data, data_path = "./data")
            logging.info(f"Training and Testing data saved successfully")
            logging.info("Data Transformation completed successfully.")

        except Exception as e:
             raise MyException(e, sys)

if __name__ == "__main__":
    obj = DataTransformation()
    obj.main()