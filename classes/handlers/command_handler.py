from classes.utilities.commands_list import CommandsList
from classes.utilities.class_modifier import ClassModifier
from classes.utilities.array_modifier import ArrayModifier
from classes.handlers.log_handler import LogHandler

import sys

class CommandHandler():
    
    global command_map
    command_map = CommandsList.__dict__

    

    def handle_help_command(self, command):
        pass

    
            
            
    def finde_first_command(self, command_list):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, 'Finding first command', '')
        first_command = command_list[0]
        for key , value in command_map.items():
            if value == first_command:
                LogHandler.debug_log(self, function_name, 'key: ', key)
                command_list[0] = key
                return command_list 
                
                
                
    def return_first_command(self, command_list):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, 'command_list', command_list)
        first_command = command_list[0]
        LogHandler.debug_log(self, function_name, 'first_command: ', first_command)
        return first_command
        
        
    def return_app_command(self, command_list):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')
        app_command = command_list[1]
        LogHandler.debug_log(self, function_name, 'app_command: ', app_command)
        return app_command
    
    def return_keyword(self, command_list):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')
        keyword = ArrayModifier.clean_char_in_list_of_string(self, command_list)
        LogHandler.debug_log(self, function_name, 'keyword: ', keyword)
        return keyword
