import os
import sys
import pickle
sys.path.insert(0, 'D:\Laptop_Price_Prediction\src')
from logger import logging
from exception import CustomException

def save_object(path,object):
    try:
        dir_path=os.path.dirname(path)
        os.makedirs(dir_path)
        
        with open(path,'wb') as file_obj:
            pickle.dump(object,file_obj)
    except Exception as e:
        logging.info('ERROR OCCURED IN SAVING THE OBJECT')
        raise CustomException(e,sys)

def load_object(path):
    try:
        with open(path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('ERROR OCCURED DURING LOADING THE OBJECT')
        raise CustomException(e,sys)