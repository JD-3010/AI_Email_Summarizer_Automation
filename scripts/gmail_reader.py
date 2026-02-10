import os
import json

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_emails():
    creds = None

    # 🔹 Load existing token if present
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # 🔹 If no token, run OAuth flow
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES
        )
        creds = flow.run_local_server(port=0)

        # 🔹 Save token for future runs
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(
        userId='me',
        maxResults=10
    ).execute()

    messages = results.get('messages', [])

    emails = []
    for msg in messages:
        txt = service.users().messages().get(
            userId='me',
            id=msg['id']
        ).execute()
        snippet = txt.get('snippet')
        emails.append(snippet)

    return emails


if __name__ == "__main__":
    emails = get_emails()
    for e in emails:
        print(e)
