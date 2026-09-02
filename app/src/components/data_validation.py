import os
import sys
import json
import yaml

import pandas as pd
from pandas import DataFrame

from app.src.utils.exception import MyException
from app.src.utils.logger import logging
from app.src.utils.config_reader import read_yaml_file
from app.src.constants import (TARGET_COLUMN,
                               SCHEMA_FILE_PATH, 
                               DATA_INGESTION_DIR_NAME, 
                               DATA_INGESTION_TRAIN_FILE_NAME, 
                               DATA_INGESTION_TEST_FILE_NAME, 
                               DATA_VALIDATION_DIR_NAME, 
                               DATA_VALIDATION_REPORT_FILE_NAME, 
                               ARTIFACT_DIR
)

class DataValidation:
    def __init__(self):
        try:
            self.train_file_path = os.path.join(ARTIFACT_DIR, DATA_INGESTION_DIR_NAME, DATA_INGESTION_TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(ARTIFACT_DIR, DATA_INGESTION_DIR_NAME, DATA_INGESTION_TEST_FILE_NAME)
            self.validation_report_file_path = os.path.join(ARTIFACT_DIR, DATA_VALIDATION_DIR_NAME,DATA_VALIDATION_REPORT_FILE_NAME)
            self._schema_config = read_yaml_file(file_path = SCHEMA_FILE_PATH)

        except Exception as e:
            raise MyException(e, sys)

    def load_data(self, file_path: str):
        try:
            df = pd.read_csv(file_path)
            logging.info("Data loaded successfully")
            return df

        except Exception as e:
            raise MyException(e, sys)

    def get_expected_column(self):
        try:
            excepted_columns = []
            for column in self._schema_config["columns"]:
                column_name = list(column.keys())[0]
                excepted_columns.append(column_name)
            return excepted_columns

        except Exception as e:
            raise MyException(e, sys)

    def is_column_exist(self, df: DataFrame, dataset_name: str):
        try:
            excepted_column = self.get_expected_column()
            missing_columns = [column for column in excepted_column if column not in df.columns]
            if missing_columns:
                logging.error(f"{dataset_name}: Missing columns: {missing_columns}")
            else:
                logging.info(f"{dataset_name}: All required columns are present")
            return missing_columns

        except Exception as e:
            raise MyException(e, sys)

    def validate_target_column(self, df: DataFrame, dataset_name: str):
        try:
            if TARGET_COLUMN not in df.columns:
                logging.error(f"{dataset_name}: Missing columns: {TARGET_COLUMN}")
                return False
            logging.info(f"{dataset_name}: Target Column: {TARGET_COLUMN} is present")
            return True

        except Exception as e:
            raise MyException(e, sys)

    def main(self):
        try:
            logging.info("Data Validation Started.")
            validation_error_message = []

            # Load Data
            train_data = self.load_data(self.train_file_path)
            test_data = self.load_data(self.test_file_path)

            # Checking Validation on Training data
            train_missing_columns = self.is_column_exist(df = train_data, dataset_name = "Training Data")
            train_target_column = self.validate_target_column(df = train_data, dataset_name = "Training Data")

            if train_missing_columns:
                validation_error_message.append(f"Missing columns in training data: {train_missing_columns}")

            if not train_target_column:
                validation_error_message.append(f"Target columns: {TARGET_COLUMN} is missing in training data")

            # Checking Validation on Testing Data
            test_missing_columns = self.is_column_exist(df = test_data, dataset_name = "Testing Data")
            test_target_column = self.validate_target_column(df = test_data, dataset_name = "Testing Data")

            if test_missing_columns:
                validation_error_message.append(f"Missing columns in testing data: {test_missing_columns}")

            if not test_target_column:
                validation_error_message.append(f"Target columns: {TARGET_COLUMN} is missing in testing data")

            # Validation Report
            validation_status = len(validation_error_message) == 0

            if validation_status:
                message = "Data validation completed successfully. " \
                "All required columns and target columns are present in training and testing data"
                logging.info(message)
            else:
                message = " ".join(validation_error_message)
                logging.error(f"Data validation failed: {message}")

            report_directory = os.path.dirname(self.validation_report_file_path)
            if report_directory:
                os.makedirs(report_directory, exist_ok=True)

            validation_report = {
                "validation_status": validation_status,
                "message": message,

                "train_data": {
                    "missing_columns": train_missing_columns,
                    "target_column": TARGET_COLUMN,
                    "target_column_present": train_target_column
                },

                "test_data": {
                    "missing_columns": test_missing_columns,
                    "target_column": TARGET_COLUMN,
                    "target_column_present": test_target_column
                }
            }

            # Save Reports
            with open(self.validation_report_file_path, "w") as report_file:
                json.dump(validation_report, report_file, indent=4)

            logging.info("Data validation report created successfully.")

            return {
                "validation_status": validation_status,
                "message": message,
                "validation_report_file_path": self.validation_report_file_path
            }

        except Exception as e:
            raise MyException(e, sys) from e
