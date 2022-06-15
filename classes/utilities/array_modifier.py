from classes.handlers.log_handler import LogHandler

import re
import sys

class ArrayModifier():
    
    
    def clean_char_in_list_of_string(self, string_list):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, '', '')
        LogHandler.debug_log(self, function_name, 'string_list: ', string_list)
        index = None
        new_string = None
        for string in string_list:
            if string.startswith('(') or string.startswith(')'):
                new_string = string.replace('(','').replace(')', '')
                index = string_list.index(string)
            if new_string != None: 
                return new_string
        