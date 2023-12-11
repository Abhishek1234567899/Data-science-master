import sys

class customexception(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        # knowing in which script errer does take place and on wbhich line and on which place 
        _,_,exc_tb=error_details=error_details.exc_info()
        # exc tracing the complete execusion

        self.exc_tb= exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
    
    def ___str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name,self.lineno,str(self.error_message))


        
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        raise customexception(e,sys) # sys=system

