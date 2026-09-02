import sys
import yaml

from app.src.utils.exception import MyException

def read_yaml_file(file_path: str):
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise MyException(e, sys) from e

