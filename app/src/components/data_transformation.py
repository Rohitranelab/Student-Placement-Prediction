import os
import sys
import pandas as pd

from app.src.utils.exception import MyException
from app.src.utils.logger import logging
from app.src.constants import (COLUMN_NAME,
                               ARTIFACT_DIR,
                               TARGET_COLUMN,
                               DATA_INGESTION_DIR_NAME,
                               DATA_INGESTION_TRAIN_FILE_NAME,
                               DATA_INGESTION_TEST_FILE_NAME,
                               DATA_TRANSFORMATION_DIR_NAME, 
                               DATA_TRANSFORMATION_TRAIN_FILE_NAME, 
                               DATA_TRANSFORMATION_TEST_FILE_NAME)

class DataTransformation:
    def __init__(self):
        try:
            self.train_file_path = os.path.join(ARTIFACT_DIR, DATA_INGESTION_DIR_NAME, DATA_INGESTION_TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(ARTIFACT_DIR, DATA_INGESTION_DIR_NAME, DATA_INGESTION_TEST_FILE_NAME)

        except Exception as e:
            raise MyException(e, sys)
        
    def load_data(self, file_path: str):
        try:
            df = pd.read_csv(file_path)
            logging.info("Data loaded successfully")
            return df

        except Exception as e:
            raise MyException(e, sys)

    def remove_column(self, df: pd.DataFrame, column_name: list):
            try:
                remove_df_columns = [col for col in column_name if col in df.columns]
                df.drop(columns = remove_df_columns, axis = 1, inplace = True)
                logging.info(f"Removed columns: {remove_df_columns}")
                return df
    
            except Exception as e:
                raise MyException(e, sys)

    def save_data(self, train_data: pd.DataFrame, test_data: pd.DataFrame, data_path: str):
        try:
            raw_data = os.path.join(data_path, DATA_TRANSFORMATION_DIR_NAME)
            os.makedirs(raw_data, exist_ok = True)

            train_path = os.path.join(raw_data, DATA_TRANSFORMATION_TRAIN_FILE_NAME)
            test_path = os.path.join(raw_data, DATA_TRANSFORMATION_TEST_FILE_NAME)

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
            train_data = self.load_data(file_path = self.train_file_path)
            test_data = self.load_data(file_path = self.test_file_path)
            logging.info("Training and Testing data loaded successfully")

            # Remove Columns
            train_data = self.remove_column(train_data, column_name = COLUMN_NAME)
            logging.info(f"Dataset shape after removing columns: {train_data.shape}")

            test_data = self.remove_column(test_data, column_name = COLUMN_NAME)
            logging.info(f"Dataset shape after removing columns: {test_data.shape}")

            # Checking target column are present or not in training and testing data

            if TARGET_COLUMN not in train_data.columns:
                logging.info(f"{TARGET_COLUMN} are not present in training data")

            if TARGET_COLUMN not in test_data.columns:
                logging.info(f"{TARGET_COLUMN} are not present in testing data")

            # Saving processed data
            self.save_data(train_data = train_data, test_data = test_data, data_path = ARTIFACT_DIR)
            logging.info(f"Training and Testing data saved successfully")
            logging.info("Data Transformation completed successfully.")

        except Exception as e:
             raise MyException(e, sys)