import sys

from app.src.utils.exception import MyException
from app.src.utils.logger import logging

from app.src.components.data_ingestion import DataIngestion
from app.src.components.data_transformation import DataTransformation
from app.src.components.model_building import ModelBuilding
from app.src.components.model_evaluation import ModelEvaluation

class TrainingPrediction:
    def run_pipeline(self):
        try:
            logging.info("=" * 70)
            logging.info("TRAINING AND PREDICTION PIPELINE STARTED")
            logging.info("=" * 70)

            logging.info("STEP 1: Starting Data Ingestion")
            data_ingestion = DataIngestion()
            data_ingestion.main()
            logging.info("STEP 1: Data Ingestion completed successfully")

            logging.info("STEP 2: Starting Data Transformation")
            data_transformation = DataTransformation()
            data_transformation.main()
            logging.info("STEP 2: Data Transformation completed successfully")

            logging.info("STEP 3: Starting Model Building")
            model_building = ModelBuilding()
            model_building.main()
            logging.info("STEP 3: Model Building completed successfully")

            logging.info("STEP 4: Starting Model Evaluation")
            model_evaluation = ModelEvaluation()
            model_evaluation.main()
            logging.info("STEP 4: Model Evaluation completed successfully")

            logging.info("=" * 70)
            logging.info("TRAINING AND PREDICTION PIPELINE COMPLETED SUCCESSFULLY")
            logging.info("=" * 70)

        except Exception as e:
            logging.error("Training and Prediction Pipeline Failed")
            raise MyException(e, sys)

if __name__ == "__main__":
    obj = TrainingPrediction()
    obj.run_pipeline()