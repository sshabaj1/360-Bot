from classes.utilities.static_variables import StaticVariables
from classes.handlers.input_handler import InputHandler
from classes.handlers.log_handler import LogHandler
import sys





class MainApp():
    
    input_handler = InputHandler()



    def run(self):
        function_name = sys._getframe().f_code.co_name
        LogHandler.create_log_file(self)
        print(StaticVariables.WELLCOME_MESSAGE_STRING)
        input_command = self.input_handler.await_input()
        LogHandler.debug_log(self, function_name, 'input_command: ',input_command)
        self.input_handler.split_input(input_command)
        self.rerun()

    def rerun(self):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, 'rerun','')
        input_command = self.input_handler.await_input()
        self.input_handler.split_input(input_command)
        self.rerun()