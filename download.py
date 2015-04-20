#!/usr/bin/python3
# Download Files 
from apiclient import errors


def download_file(service, drive):
    download = drive.get('downloadUrl')
    if download:
        resp, content = service._http.request(download)
        if resp.status == 200:
            print 'Status: %s' % resp
            return content
        else:
            print 'An error occurred: %s' % resp
            return None
    else:
        return None
