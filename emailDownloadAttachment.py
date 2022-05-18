# Change these gmail settings for gmail to be configured for python
# https://support.google.com/mail/answer/7104828?hl=en&visit_id=637860841480990273-2981824608&rd=2
# https://support.google.com/accounts/answer/3466521?p=app_notverified
# https://developers.google.com/gmail/api/quickstart/python
# https://developers.google.com/resources/api-libraries/documentation/gmail/v1/python/latest/gmail_v1.users.messages.html#lsit


import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64

# If modifying these scopes, delete the file token.json and rerun the program
# Currently this is set to modify
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


def downloadAttachment(emailSubject):
    global creds

    # Gathering credentials from token file
    if os.path.exists('gmail_authentication_files/token.json'):
        creds = Credentials.from_authorized_user_file('gmail_authentication_files/token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Authenticate the gmail with scope and credentials
            flow = InstalledAppFlow.from_client_secrets_file(
                'gmail_authentication_files/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('gmail_authentication_files/token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)

        # listing all unread emails in the INBOX
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], q="is:unread").execute()

        messages = results.get('messages', [])
        if not messages:
            print(
                "______________________________No New Emails, Exiting Program_____________________________________________\n")
            exit(0)

        # Get Unread message count
        messageCount = len(messages)
        print("Unread Messages: " + (str)(messageCount))
        print('\nGmail Messages:')

        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            # Marking mails are read
            service.users().messages().modify(userId='me', id=message['id'],
                                              body={'removeLabelIds': ['UNREAD']}).execute()
            email_data = msg
            for i in email_data['payload']['headers']:
                name = i['name']
                if name == "Subject":
                    # only taking mails with the required subject
                    if i['value'] == emailSubject:
                        message_body = msg['snippet']
                        print(
                            '_____________________________________________________________________________________________________________\n')
                        print('Message Body: ' + message_body)
                        messageDetail = service.users().messages().get(userId='me', id=msg['id'], format='full',
                                                                       metadataHeaders=['parts']).execute()
                        messageDetailPayload = messageDetail.get('payload')
                        # Downloading attachments
                        if 'parts' in messageDetailPayload:
                            for msgPayload in messageDetailPayload['parts']:
                                file_name = msgPayload['filename']
                                body = msgPayload['body']
                                if 'attachmentId' in body:
                                    attachment_id = body['attachmentId']
                                    response = service.users().messages().attachments().get(
                                        userId='me',
                                        messageId=msg['id'],
                                        id=attachment_id
                                    ).execute()

                                    attachment_content = base64.urlsafe_b64decode(response.get('data').encode('UTF-8'))

                                    with open(os.path.join(os.getcwd(), 'InputImage', file_name), 'wb') as _f:
                                        _f.write(attachment_content)
                                        print(f'File {file_name} download completed.')
                if name == 'From':
                    from_email = i['value']
                    print("From address: " + from_email)
                if name == 'To':
                    from_email = i['value']
                    print("To address: " + from_email + '\n')
    except HttpError as error:
        print(f'An error occurred: {error}')
