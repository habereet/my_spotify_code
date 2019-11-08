import sys
import spotipy
import spotipy.util as util

from credentials import my_client_id, my_client_secret, my_redirect_uri, username

def search(spotipyToken, query, target_market="US"):
    searchResults = spotipyToken.search(q=query, market=target_market)


def get_user_name(locals):
    if 'username' in locals:
        username = locals["username"]
    elif len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()
        
    print(f'Username to use: {username}\n')
    return username

def get_token(my_vars):
    scope = 'user-library-read'
    token = util.prompt_for_user_token(get_user_name(my_vars), scope, my_client_id, my_client_secret, my_redirect_uri)
    return token
    
def get_saved_tracks(my_vars):
    token = get_token(my_vars)
    
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            if track['explicit'] == False:
                print(track['name'] + ' - ' + track['artists'][0]['name'])
    else:
        print("Can't get token for", username)

def main(my_vars):
    get_saved_tracks(my_vars)

if __name__== "__main__":
    main(vars())