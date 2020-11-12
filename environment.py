from dotenv import load_dotenv
import spotipy
import spotipy.util as util
import os


# Variables class will store API secrets from stored in .env
# TODO implement try/catch in case .env isn't set up correctly
class Variables:
    def __init__(self, commandLineArgs):
        load_dotenv()
        self.set_clientID(os.getenv("client_id"))
        self.set_clientSecret(os.getenv("client_secret"))
        self.set_redirectURL(os.getenv("redirect_url"))
        self.set_username(commandLineArgs)
        self.set_token()

    def set_username(self, commandLineArgs):
        try:
            username = os.getenv("username")
            if username is None:
                raise ValueError()
            else:
                self.username = username
        except ValueError:
            if len(commandLineArgs) > 1:
                self.username = commandLineArgs[1]
            else:
                print("Username not provided")
                sys.exit()

    def set_clientID(self, clientID):
        self.clientID = clientID

    def set_clientSecret(self, clientSecret):
        self.clientSecret = clientSecret

    def set_redirectURL(self, redirectURL):
        self.redirectURL = redirectURL

    def set_token(self):
        scope = 'user-library-read'
        self.token = util.prompt_for_user_token(self.username,
                                                scope,
                                                self.clientID,
                                                self.clientSecret,
                                                self.redirectURL)
