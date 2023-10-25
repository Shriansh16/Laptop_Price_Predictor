import os
import sys
import pandas as pd
import numpy as np
sys.path.insert(0, 'D:\Laptop_Price_Prediction\src')
from logger import logging
from exception import CustomException
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path=os.path.join('artifacts','raw.csv')
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        



