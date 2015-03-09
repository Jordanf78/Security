#!/usr/bin/python

import httplib2
import pprint
from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

SCOPE = "https://www.googleapis.com/auth/drive'"
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
FILENAME = "chirag.txt"
TITLE = "New Document"

http = httplib2.http()

# inserting a file
main_file = apiclient.http.fileUpload(FILENAME) 
