import logging
import csv
import os

def setup_logger(log_path):
    logger = logging.getLogger('train_logger')
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        fh = logging.FileHandler(log_path)
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s,%(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger

def log_to_csv(csv_path, row):
    file_exists = os.path.isfile(csv_path)
    with open(csv_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['doc_id', 'class', 'confidentiality_level', 'confidence_score'])
        writer.writerow(row)
