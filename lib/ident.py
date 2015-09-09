import requests
import json
import warnings
import sys


class IdentCall(object):
    DEF_URL = "https://identity.api.rackspacecloud.com"

    def __init__(self, username="", apikey="", password="", endpoint=DEF_URL):

        self.endpoint = endpoint
        self.password = password
        self.apikey = apikey
        self.username = username
        self.KEY_AUTH = False
        warnings.filterwarnings('ignore', module='requests')

        if len(self.username) and len(self.apikey):
            #  username and apikey was passed in init
            self.KEY_AUTH = False
            self.set_auth(username=self.username, apikey=self.apikey)
            #  self.authNameAndKey(username, apikey)
        elif len(self.username) and len(self.password):
            # username and password passed in init
            self.KEY_AUTH = True
            self.set_auth(username=self.username, password=self.password)
            # self.authNameAndPass(username, password)
        else:
            # we got nothing
            pass

    def _set_headers(self):
        self.headers = {
            "Content-Type": "application/json"
        }

    def _set_post_data(self):
        # set the post data based on auth type
        if self.KEY_AUTH:
            self.post_data = {
                "auth": {
                    "RAX-KSKEY:apiKeyCredentials": {
                        "username": self.username,
                        "apiKey": self.apikey
                        }
                    }
                }

        else:
            self.post_data = {
                "auth": {
                    "passwordCredentials": {
                        "username": self.username,
                        "password": self.password
                    }
                }
            }

    def set_auth(self,
                 username='',
                 password='',
                 apikey='',
                 auth_now=True):
        # pass creds if not given in init
        self.username = username
        self.password = password
        self.apikey = apikey
        self.KEY_AUTH = False

        if len(self.apikey):
            self.KEY_AUTH = True
        elif len(self.password):
            self.KEY_AUTH = False
        else:
            sys.stderr.write("Need API key or Password")
            exit(2)

        self._set_post_data()

        if auth_now:
            self.auth()

    def auth(self):
        # everything is set up, auth it
        self._set_headers()
        self._set_post_data()
        self.ident_json = requests.post(self.endpoint + "/v2.0/tokens",
                                        headers=self.headers,
                                        verify=False,
                                        data=json.dumps(self.post_data))
        if self.ident_json.status_code != 200:
            sys.stderr.write("Failed: " + str(self.ident_json.status_code))
            exit(3)
            self.api_token = self.ident_json.json()['access']['token']['id']

    def call_auth(self):
        # if running auth call manually, not when passing username
        self.auth()

    def get_auth_response(self):
        return self.ident_json.json()

    def _get_token(self):
        return self.ident_json.json()['access']['token']['id']

    def get_api_token(self):
        return self.api_token

    def get_json(self):
        return self.ident_json.json()
