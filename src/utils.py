import os
import sys
import dill
import pickle

from src.exception import CustomException


def save_object(file_path, obj):
    """
    Save python object using dill.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    """
    Load python object. Try dill first, then pickle.
    """
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception:
        try:
            with open(file_path, "rb") as file_obj:
                return pickle.load(file_obj)

        except Exception as e:
            raise CustomException(e, sys)
