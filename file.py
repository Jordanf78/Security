#!/usr/bin/python3 
# Create files ftome the Drive 

class DriveState(object):
    def __init__(self, state):
        state_data = json.loads(state)
        self.action = state_data['action']
        self.ids = map(str, state_data.get('ids', []))

    def insert_file(service, title, description, mime_type):
      body = {
          'title of the file': title,
          'description of the file': description
          'mimeType': 'application/vnd.google-apps.drive-sdk',
      }
      file = service.files().insert(body=body).execute()
           print 'File ID: %s' % file['id']
