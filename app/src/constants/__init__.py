import os

# TARGET COLUMN
TARGET_COLUMN = "placement_status"

# DATA SOURCE
DATA_PATH = "https://raw.githubusercontent.com/Rohitranelab/dataset/refs/heads/main/student_placement.csv"

# COLUMNS TO REMOVE
COLUMN_NAME = ["package_range"]

# ARTIFACT DIRECTORY
ARTIFACT_DIR = "artifact"

# SCHEMA FILES
SCHEMA_FILE_PATH = os.path.join("app", "config", "schema.yaml")

# DATA INGESTION
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_TRAIN_AND_TEST_SPLIT_RATIO: float = 0.3
DATA_INGESTION_RANDOM_STATE: int = 42
DATA_INGESTION_TRAIN_FILE_NAME: str = "train.csv"
DATA_INGESTION_TEST_FILE_NAME: str = "test.csv"

# DATA VALIDATION
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "data_validation_report.json"

# DATA TRANSFORMATION
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRAIN_FILE_NAME: str = "train_processed.csv"
DATA_TRANSFORMATION_TEST_FILE_NAME: str = "test_processed.csv"

# MODEL TRAINER
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_MAX_ITER: int = 2000
MODEL_TRAINER_RANDOM_STATE: int = 42

# MODEL EVALUATION
MODEL_EVALUATION_DIR_NAME: str = "reports"
MODEL_EVALUATION_METRICS_NAME: str = "metrics"
MODEL_EVALUATION_METRICS_FILE_NAME: str = "metrics.json"