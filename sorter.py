import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

print("Loading script... please wait.") # This should appear instantly!

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def run_sorter():
    print("--- Sorter Started ---")
    service = get_gmail_service()
    
    # Targeting aaa,bbb,ccc(aaa,bbb and ccc are our target mail list) in the Inbox they might be  also keywords
    search_query = "(aaa OR bbb OR ccc) label:INBOX"
    print(f"Searching for: {search_query}...")
    
    results = service.users().messages().list(userId='me', q=search_query).execute()
    messages = results.get('messages', [])

    if not messages:
        print("Result: No emails from 'Irina' found in your Inbox.")
        return

    print(f"Result: Found {len(messages)} matching emails. Moving to Bin...")

    for msg in messages:
        try:
            service.users().messages().trash(userId='me', id=msg['id']).execute()
            print(f"Success: Message {msg['id']} moved to Bin.")
        except Exception as e:
            print(f"Error moving message {msg['id']}: {e}")

    print("--- Cleanup Finished ---")

# --- THIS PART MUST BE AT THE VERY BOTTOM AND HAVE NO SPACES ON THE LEFT ---
if __name__ == '__main__':
    run_sorter()
