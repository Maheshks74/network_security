import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_msg,error_detail:sys):
        self.error_msg=error_msg
        _,_,exc_tb=error_detail.exc_info()
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in python script name [{0}] line no [{1}] error msg [{2}]".format(self.file_name, self.lineno, self.error_msg)

    


    