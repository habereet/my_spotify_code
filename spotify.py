import sys
import os
from dotenv import load_dotenv
import spotipy
import spotipy.util as util


# Variables class will store API secrets from stored in .env
# TODO implement try/catch in case .env isn't set up correctly
class Variables:
    def __init__(self):
        load_dotenv()
        self.clientID = os.getenv("client_id")
        self.clientSecret = os.getenv("client_secret")
        self.redirectURL = os.getenv("redirect_url")


# TODO explain search
# TODO implement search
def search(spotipyToken, query, target_market="US"):
    searchResults = spotipyToken.search(q=query, market=target_market)
    print(searchResults)


# TODO explain get_user_name
def get_user_name(locals):
    try:
        load_dotenv()
        return os.getenv("username")
    except NameError:
        if len(sys.argv) > 1:
            return sys.argv[1]
        else:
            print("Username not provided")
            sys.exit()


# TOD explain get_token
def get_token(myVals, username):
    scope = 'user-library-read'
    token = util.prompt_for_user_token(username,
                                       scope,
                                       myVals.clientID,
                                       myVals.clientSecret,
                                       myVals.redirectURL)
    return token


# TODO explain get_saved_tracks
# TODO Better name values in for loop
def get_saved_tracks(token):
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            name = track['name']
            artist = track['artists'][0]['name']
            explicit = track['explicit']
            print(f"{name} - {artist}{' (Explicit)' if explicit else ''}")
    else:
        print("Can't get token for requested user")


# TODO describe workflow
def main(my_vars):
    myVals = Variables()
    username = get_user_name(my_vars)
    token = get_token(myVals, username)
    get_saved_tracks(token)


if __name__ == "__main__":
    # Pass command line, if used, to main
    main(vars())
