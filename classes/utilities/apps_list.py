from classes.apps.google_app import GoogleApp
from classes.apps.root import Root
from classes.apps.user import User
from classes.apps.youtube_app import YoutubeApp



class AppsList():
    
    youtube = YoutubeApp()
    rootApp = Root()
    userApp = User()
    googleApp = GoogleApp()