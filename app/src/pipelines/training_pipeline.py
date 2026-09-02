import sys

from app.src.utils.exception import MyException
from app.src.utils.logger import logging

from app.src.components.data_ingestion import DataIngestion
from app.src.components.data_validation import DataValidation
from app.src.components.data_transformation import DataTransformation
from app.src.components.model_building import ModelBuilding
from app.src.components.model_evaluation import ModelEvaluation

class TrainingPrediction:
    def start_data_ingestion(self):
        try:
            logging.info("STEP 1: Starting Data Ingestion")
            data_ingestion = DataIngestion()
            data_ingestion.main()
            logging.info("STEP 1: Data Ingestion completed successfully")

        except Exception as e:
            raise MyException(e, sys)

    def start_data_validation(self):
        try:
            logging.info("=" * 70)
            logging.info("STEP 2: Starting Data Validation")
            data_validation = DataValidation()
            data_validation.main()
            logging.info("STEP 2: Data Validation completed successfully")

        except Exception as e:
            raise MyException(e, sys)
        
    def start_data_transformation(self):
        try:
            logging.info("=" * 70)
            logging.info("STEP 3: Starting Data Transformation")
            data_transformation = DataTransformation()
            data_transformation.main()
            logging.info("STEP 3: Data Transformation completed successfully")

        except Exception as e:
            raise MyException(e, sys)

    def start_model_building(self):
        try:
            logging.info("=" * 70)
            logging.info("STEP 4: Starting Model Building")
            model_building = ModelBuilding()
            model_building.main()
            logging.info("STEP 4: Model Building completed successfully")

        except Exception as e:
            raise MyException(e, sys)

    def start_model_evaluation(self):
        try:
            logging.info("=" * 70)
            logging.info("STEP 5: Starting Model Evaluation")
            model_evaluation = ModelEvaluation()
            model_evaluation.main()
            logging.info("STEP 5: Model Evaluation completed successfully")

        except Exception as e:
            raise MyException(e, sys)
    
    def run_pipeline(self):
        try:
            logging.info("=" * 70)
            logging.info("TRAINING AND PREDICTION PIPELINE STARTED")
            logging.info("=" * 70)

            self.start_data_ingestion()

            self.start_data_validation()     

            self.start_data_transformation()

            self.start_model_building()

            self.start_model_evaluation()            

            logging.info("=" * 70)
            logging.info("TRAINING AND PREDICTION PIPELINE COMPLETED SUCCESSFULLY")
            logging.info("=" * 70)

        except Exception as e:
            logging.error("Training and Prediction Pipeline Failed")
            raise MyException(e, sys)