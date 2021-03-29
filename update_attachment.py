import requests
import mimetypes

CONFLUENCE_URL = 'http://localhost:6747/c747'
PAGE_ID = '1572872'
FILE = 'test58.txt'
USERNAME = 'admin'
PASSWORD = 'notpassword'
ATTACHMENT_ID = '1572876'

def update_attachment():
    url = str(CONFLUENCE_URL) + '/rest/api/content/' + \
          str(PAGE_ID) + '/child/attachment/' + \
          str(ATTACHMENT_ID) + '/data/'
    headers = {'X-Atlassian-Token': 'no-check'} #no content-type here!
    file = str(FILE)

    # determine content-type
    content_type, encoding = mimetypes.guess_type(file)
    if content_type is None:
        content_type = 'multipart/form-data'

    # provide content-type explicitly
    files = {'file': (file, open(file, 'rb'), content_type)}

    auth = (str(USERNAME), str(PASSWORD))
    r = requests.post(url, headers=headers, files=files, auth=auth)
    r.raise_for_status()

update_attachment()