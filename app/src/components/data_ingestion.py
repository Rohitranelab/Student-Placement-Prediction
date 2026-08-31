import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from app.src.utils.logger import logging
from app.src.utils.exception import MyException

class DataIngestion:
    def load_data(self, file_path: str):
        try:
            df = pd.read_csv(file_path)
            logging.info("Load data successfully")
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
            raw_data = os.path.join(data_path, "raw")
            os.makedirs(raw_data, exist_ok = True)

            train_path = os.path.join(raw_data, "train.csv")
            test_path = os.path.join(raw_data, "test.csv")

            train_data.to_csv(train_path, index = False)
            test_data.to_csv(test_path, index = False)

            logging.info(f"Training data saved to: {train_path}")
            logging.info(f"Testing data saved to: {test_path}")

        except Exception as e:
            raise MyException(e, sys)

    def main(self):
        try:
            logging.info("Data Ingestion Started.")
            data_url = ("https://raw.githubusercontent.com/Rohitranelab/dataset/refs/heads/main/student_placement.csv")

            # Load Data
            df = self.load_data(file_path = data_url)
            logging.info("Data loaded successfully")
            logging.info(f"Data shape: {df.shape}")

            # Remove Columns
            column_name = ["package_range"]
            df = self.remove_column(df, column_name)
            logging.info(f"Dataset shape after removing columns: {df.shape}")

            # Train-Test Split
            train_data, test_data = train_test_split(df, test_size = 0.3, random_state = 42)
            logging.info(f"Train data shape: {train_data.shape}")
            logging.info(f"Test data shape: {test_data.shape}")

            # Save Data
            self.save_data(train_data = train_data, test_data = test_data, data_path = "./data")
            logging.info("Data Ingestion completed successfully.")

        except Exception as e:
            raise MyException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.main()