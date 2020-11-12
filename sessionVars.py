from dotenv import load_dotenv
import spotipy.util as util
import os
import sys


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
        try:
            if clientID is None:
                raise ValueError()
            else:
                self.clientID = clientID
        except ValueEreor:
            print("Client ID not provided")
            sys.exit()

    def set_clientSecret(self, clientSecret):
        try:
            if clientSecret is None:
                raise ValueError
            else:
                self.clientSecret = clientSecret
        except ValueError:
            print("Client Secret not provided")
            sys.exit()

    def set_redirectURL(self, redirectURL):
        self.redirectURL = redirectURL

    def set_token(self):
        scope = 'user-library-read'
        self.token = util.prompt_for_user_token(self.username,
                                                scope,
                                                self.clientID,
                                                self.clientSecret,
                                                self.redirectURL)
