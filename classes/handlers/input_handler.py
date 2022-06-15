from ast import keyword
from classes.utilities.static_variables import StaticVariables
from classes.handlers.command_handler import CommandHandler
from classes.connectors.main_connector import MainConnector
from classes.handlers.log_handler import LogHandler
import re
import sys

class InputHandler():

    

    def await_input(self):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')
        input_command = input(StaticVariables.INPUT_AWAIT_STRING)
        LogHandler.debug_log(self, function_name, 'input_command: ', input_command)
        return input_command
        

    def split_input(self, command):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')
        connector_map = {}
        full_command = command
        LogHandler.debug_log(self, function_name, 'full_command: ', full_command)
        command_list = re.split(StaticVariables.COMMAND_SPLIT_REGEX, full_command)
        LogHandler.debug_log(self, function_name, 'command_list: ', command_list)
        cmd_list = CommandHandler.finde_first_command(self,command_list)
        first_command = CommandHandler.return_first_command(self, cmd_list)
        connector_map["command"] = first_command
        LogHandler.debug_log(self, function_name, 'first_command: ', first_command)
        app_command = CommandHandler.return_app_command(self, command_list)
        connector_map["app"] = app_command
        keyword = CommandHandler.return_keyword(self, command_list)
        connector_map["keyword"] = keyword
        MainConnector.connect_app(self,connector_map)

        

    

    
    
        
