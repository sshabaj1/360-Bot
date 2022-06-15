import imp
import pywhatkit
from classes.handlers.log_handler import LogHandler
import sys


class YoutubeApp():
    

    def connect(self, context):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, 'connected', '')
        if context["command"] == "PLAY_COMMAND":
            self.play(context["keyword"])

    def play(self, search_keyword):
        function_name = sys._getframe().f_code.co_name
        LogHandler.debug_log(self, function_name, 'play/keyword: ', search_keyword)
        pywhatkit.playonyt(search_keyword);
        LogHandler.info_log( self, function_name, 'playing', '')


        
        
    