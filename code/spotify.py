import sys
from sessionVars import Variables
import spotipy


# TODO explain search
# TODO implement search
def search(spotipyToken, query, target_market="US"):
    searchResults = spotipyToken.search(q=query, market=target_market)
    print(searchResults)


# TODO explain get_saved_tracks
# TODO Better name values in for loop
def get_saved_tracks(myVals):
    try:
        sp = spotipy.Spotify(auth=myVals.get_token())
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            name = track['name']
            artist = track['artists'][0]['name']
            explicit = track['explicit']
            print(f"{name} - {artist}{' (Explicit)' if explicit else ''}")
    except Exception:
        print(f"Token doesn't exist for {myVals.get_username()}")


# TODO describe workflow
def main():
    myVals = Variables(sys.argv)
    get_saved_tracks(myVals)


if __name__ == "__main__":
    main()
