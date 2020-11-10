import sys
import os
from dotenv import load_dotenv
import spotipy
import spotipy.util as util


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


# TODO explain search
# TODO implement search
def search(spotipyToken, query, target_market="US"):
    searchResults = spotipyToken.search(q=query, market=target_market)
    print(searchResults)


# TOD explain get_token
def get_token(myVals):
    scope = 'user-library-read'
    token = util.prompt_for_user_token(myVals.username,
                                       scope,
                                       myVals.clientID,
                                       myVals.clientSecret,
                                       myVals.redirectURL)
    return token


# TODO explain get_saved_tracks
# TODO Better name values in for loop
def get_saved_tracks(myVals):
    if myVals.token:
        sp = spotipy.Spotify(auth=myVals.token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            name = track['name']
            artist = track['artists'][0]['name']
            explicit = track['explicit']
            print(f"{name} - {artist}{' (Explicit)' if explicit else ''}")
    else:
        print(f"Token doesn't exist for {myVals.username}")


# TODO describe workflow
def main():
    myVals = Variables(sys.argv)
    get_saved_tracks(myVals)


if __name__ == "__main__":
    # Pass command line, if used, to main
    main()
