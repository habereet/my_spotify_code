import sys
import spotipy
import spotipy.util as util

from credentials import my_client_id, my_client_secret, my_redirect_uri, username

scope = 'user-library-read'

if 'username' in locals():
    print(f'Username to use: {username}\n')
elif len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope, my_client_id, my_client_secret, my_redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print(track['name'] + ' - ' + track['artists'][0]['name'])
else:
    printO("Can't get token for", username)