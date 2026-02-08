import os
import sys
<<<<<<< HEAD
=======

import numpy as np
import pandas as pd
>>>>>>> c4ffba8e49156847fd1b2bafcc3516771db20e64
import dill

from src.exception import CustomException

<<<<<<< HEAD

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
=======
def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)
>>>>>>> c4ffba8e49156847fd1b2bafcc3516771db20e64

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
<<<<<<< HEAD
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
=======
        raise CustomException(e, sys)        
>>>>>>> c4ffba8e49156847fd1b2bafcc3516771db20e64
