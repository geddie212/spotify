import requests
from urllib.parse import urlencode
from flask import Flask
app = Flask(__name__)

@app.route("/spotify/callback")
def spotify_callback():
    return "You finally called me back!"


USER_ID = '31ldamf4qfvtxkjnpmpv2w3wwfbq'
CLIENT_ID = '553bc459600d4903babcfdec0b3f09dd'
ENPOINT = f'https://api.spotify.com/v1/users/{USER_ID}/playlists'

auth_url = 'https://accounts.spotify.com/authorize'
scopes_params = urlencode({
    'client_id': CLIENT_ID,
    'scope': 'playlist-modify-private',
    'redirect_uri': 'http://127.0.0.1:5000/spotify/callback',
    'response_type': 'code'
})

scope_url = auth_url+'?'+scopes_params

print(scope_url)
