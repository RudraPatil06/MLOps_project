import sys
from src.logger import logging


def error_message_detail(error, error_detail: sys):
    try:
        _, _, exc_tb = error_detail.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = (
            f"Error occurred in python script name [{file_name}] "
            f"line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
        )
        return error_message
    except Exception as e:
        return f"Error while creating error message: {str(e)}"


class CustomException(Exception):
    def __init__(self, error, error_detail=None):
        super().__init__(error)
        self.error = error
        self.error_detail = error_detail or sys

    def __str__(self):
        return error_message_detail(self.error, self.error_detail)

