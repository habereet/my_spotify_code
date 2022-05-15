Some code that I'm building to work within the Spotify API and do things.

Uses [spotipy](https://spotipy.readthedocs.io) to interact with the API.

To get started
* Create an app in the [Spotify Developer's Pages](https://developer.spotify.com/documentation/general/guides/app-settings/)
* Clone the repository
* Install the requirements:
  ```
  pip install -r requirements.txt
  ```
* Store your app's data in a file located at the root of the repository called .env including the following:
    ```
    client_id=client_id_from_spotify_app
    client_secret=client_secret_from_spotify_app
    redirect_url=redirect_URI_from_app
    ```
* You will you need to specify a Spotify username that you have the password to. You have two options to do this:
  * If you will only be using this for yourself, you can add the following to .env:
    ```
    username=Spotify_user_to_use
    ```
  * If you don't want to specify a user in the .env file, specify it at runtime from the command line:
    ```
    python spotify.py Spotify_user_to_use
    ```

* Depending on your IDE, you'll need to open a URL specified by spotipy and enter or click on a redirect URL. Once you've done that, you should be good to go.