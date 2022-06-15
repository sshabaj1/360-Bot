from classes.utilities.apps_list import AppsList
from classes.handlers.log_handler import LogHandler
import imp
import sys



class MainConnector():

    global apps_map
    apps_map = AppsList.__dict__
    
    def connect_app(self, command_map):
        function_name = sys._getframe().f_code.co_name
        LogHandler.info_log(self, function_name, 'Connecting','')
        app = command_map["app"]
        context = {"command":command_map["command"], "keyword":command_map["keyword"]}
        for key, value in apps_map.items():
            if key == app:
                value.connect(context)
        
            
    