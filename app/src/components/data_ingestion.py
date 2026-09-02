import os
import sys
import pandas as pd

from sklearn.model_selection import train_test_split

from app.src.utils.logger import logging
from app.src.utils.exception import MyException
from app.src.constants import (DATA_PATH, ARTIFACT_DIR,
                           DATA_INGESTION_DIR_NAME, 
                           DATA_INGESTION_TRAIN_AND_TEST_SPLIT_RATIO,
                           DATA_INGESTION_TRAIN_FILE_NAME,
                           DATA_INGESTION_TEST_FILE_NAME,
                           DATA_INGESTION_RANDOM_STATE)

class DataIngestion:
    def load_data(self, file_path: str):
        try:
            df = pd.read_csv(file_path)
            logging.info("Data loaded successfully")
            return df

        except Exception as e:
            raise MyException(e, sys)

    def split_data(self, df: pd.DataFrame):
        try:
            logging.info("Start splitting data into train and test set")
            train_data, test_data = train_test_split(df, 
                                                     test_size = DATA_INGESTION_TRAIN_AND_TEST_SPLIT_RATIO, 
                                                     random_state = DATA_INGESTION_RANDOM_STATE)
            logging.info(f"Training data shape: {train_data.shape}")
            logging.info(f"Testing data shape: {test_data.shape}")
            return train_data, test_data
        
        except Exception as e:
            raise MyException(e, sys)

    def save_data(self, train_data: pd.DataFrame, test_data: pd.DataFrame, data_path: str):
        try:
            raw_data = os.path.join(data_path, DATA_INGESTION_DIR_NAME)
            os.makedirs(raw_data, exist_ok = True)

            train_path = os.path.join(raw_data, DATA_INGESTION_TRAIN_FILE_NAME)
            test_path = os.path.join(raw_data, DATA_INGESTION_TEST_FILE_NAME)

            train_data.to_csv(train_path, index = False)
            test_data.to_csv(test_path, index = False)

            logging.info(f"Training data saved to: {train_path}")
            logging.info(f"Testing data saved to: {test_path}")

        except Exception as e:
            raise MyException(e, sys)

    def main(self):
        try:
            logging.info("Data Ingestion Started.")
            
            # Load Data
            df = self.load_data(file_path = DATA_PATH)
            logging.info("Data loaded successfully")
            logging.info(f"Data shape: {df.shape}")

            # Train-Test Split
            train_data, test_data = self.split_data(df)
            logging.info("Complete split data into train and test set")

            # Save Data
            self.save_data(train_data = train_data, test_data = test_data, data_path = ARTIFACT_DIR)
            logging.info("Data Ingestion completed successfully.")

        except Exception as e:
            raise MyException(e, sys)