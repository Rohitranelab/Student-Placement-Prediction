import logging
import os
from logging.handlers import RotatingFileHandler

LOGS_PATH = "logs"
LOG_FILE = "log_info.log"
MAX_LOG_FILE = 5 * 1024 * 1024
BACKUP_COUNT = 3

os.makedirs(LOGS_PATH, exist_ok = True)
log_file_path = os.path.join(LOGS_PATH, LOG_FILE)

def configure_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s | %(filename)s | %(message)s" )

    file_handler = RotatingFileHandler(log_file_path, maxBytes = MAX_LOG_FILE, backupCount = BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

configure_logger()