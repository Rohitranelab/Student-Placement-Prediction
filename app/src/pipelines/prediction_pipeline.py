import os
import sys
import pickle

import pandas as pd

from app.src.utils.logger import logging
from app.src.utils.exception import MyException
from app.src.constants import (ARTIFACT_DIR,
                               MODEL_TRAINER_DIR_NAME,
                               MODEL_TRAINER_TRAINED_MODEL_NAME)

class PredictionPipeline:
    def __init__(self,
                 cgpa, 
                 projects, 
                 communication_skills, 
                 internship, 
                 programming_skills, 
                 technical_skills, 
                 certifications,
                 aptitude,
                 interview_score):
        try:
            self.cgpa = cgpa
            self.projects = projects
            self.communication_skills = communication_skills
            self.internship = internship
            self.programming_skills = programming_skills
            self.technical_skills = technical_skills
            self.certifications = certifications
            self.aptitude = aptitude
            self.interview_score = interview_score

        except Exception as e:
            raise MyException(e, sys)

    def get_data_into_dict(self):
        try:
            logging.info("Converting student prediction data into dictionary")
            input_data = {
                "cgpa" : [self.cgpa],
                "projects" : [self.projects],
                "communication_skills" : [self.communication_skills],
                "internship" : [self.internship],
                "programming_skills" : [self.programming_skills],
                "technical_skills" : [self.technical_skills],
                "certifications" : [self.certifications],
                "aptitude" : [self.aptitude],
                "interview_score" : [self.interview_score]
            }
            logging.info("Student prediction data dictionary created")
            return input_data

        except Exception as e:
            raise MyException(e, sys)

    def get_data_into_dataframe(self):
        try:
            logging.info("Converting dictionary data into DataFrame")
            data = self.get_data_into_dict()
            df = pd.DataFrame(data)
            logging.info("Converted dictionary data into DataFrame successfully")
            return df

        except Exception as e:
            raise MyException(e, sys)

class Prediction:
    def __init__(self):
        try:
            self.model_path = os.path.join(ARTIFACT_DIR, MODEL_TRAINER_DIR_NAME, MODEL_TRAINER_TRAINED_MODEL_NAME)

        except Exception as e:
            raise MyException(e, sys)

    def load_model(self, model_path):
        try:
            logging.info("Model loading started")
            with open(model_path, "rb") as file:
                model = pickle.load(file)
            logging.info("Model loaded successfully")
            return model

        except Exception as e:
            raise MyException(e, sys)

    def predict(self, df: pd.DataFrame):
        try:
            logging.info("Entered predict method of Prediction class")
            logging.info(f"Loading model from: {self.model_path}")
            model = self.load_model(model_path = self.model_path)
            result = model.predict(df)
            logging.info(f"Prediction result: {result}")
            logging.info("Prediction completed successfully")
            return result

        except Exception as e:
            raise MyException(e, sys)
        