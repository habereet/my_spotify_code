import sys
from spotipy import oauth2
from sessionVars import Variables


def connectoauth(myVals):
    sp_oauth = oauth2.SpotifyOAuth(
                                    myVals.clientID,
                                    myVals.clientSecret,
                                    myVals.redirectURL,
                                    scope="",
                                    cache_path=""
                                  )
    print(sp_oauth)


# TODO describe workflow
def main():
    myVals = Variables(sys.argv)
    connectoauth(myVals)


if __name__ == "__main__":
    main()
