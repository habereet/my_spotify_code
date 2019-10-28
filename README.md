Some code that I'm building to work within the Spotify API and do things (that I want).

Uses [spotipy](https://spotipy.readthedocs.io) to interact with the API.

To get started
- Create an app in the [Spotify Developer's Pages](https://developer.spotify.com/documentation/general/guides/app-settings/)
- Store your app's data in a file located at the root of the repository called credentials.py including the following:
    ```
    my_client_id = 'client_id_from_spotify_app'
    my_client_secret = 'client_secret_from_spotify_app'
    my_redirect_uri = 'redirect_URI_from_app'
    ```
- Install the requirements:
  ```
  pip install -r requirements.txt
  ```
- If you will only be using this for yourself, you can add the following:
  - To credentials.py:
    ```
    username = 'your_username'
    ```
  - To spotify.py:
    ```
    from credentials.py import username
    ```
 
 
To run this, if you are working with just your Spotify user:
 ```
 python spotify.py
 ```
Or, if you don't want to specify a certain user in the code:
  ```
  python spotify.py Spotify_user_to_use
  ```
