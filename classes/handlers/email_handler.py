from classes.utilities.static_variables import StaticVariables
from classes.handlers.log_handler import LogHandler
from env_config import EnvConfig

import sys
import smtplib, ssl

class EmailHandler():
    
    
    
    def send_email(self, email, msg):
        function_name = sys._getframe().f_code.co_name
        LogHandler.debug_log(self, function_name, '', '')
        port = 587  # For starttls
        smtp_server = EnvConfig.SMTP_SERVER
        sender_email = EnvConfig.COBRA_EMAIL
        receiver_email = email
        password = EnvConfig.EMAIL_PASSWORD
        message = msg
        
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message) 