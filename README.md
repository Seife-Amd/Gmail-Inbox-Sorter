# Gmail-Flow: Inbox Automation & API Sorter

A Python-based utility for programmatically managing Gmail high-volume senders. This tool utilizes the **Google Gmail API** to automate the cleanup and organization of cluttered inboxes.

##  Motivation
Manual inbox management is a significant productivity drain. I developed this automation to:
- **Batch Processing:** Identify and remove low-priority marketing emails in bulk.
- **Rule-Based Sorting:** Use a modular "Toggle System" to switch between trashing or archiving to custom labels.
- **Workflow Efficiency:** Automate recurring cleanup tasks to maintain a "Zero Inbox" state.

##  Technical Architecture
- **Language:** Python 3.x
- **API Integration:** Google Gmail API (REST)
- **Authentication:** OAuth 2.0 (Desktop Flow)
- **Features:** Modular search queries, error handling, and activity logging.

##  Deployment & Setup
1. **Dependencies:** Install via `pip install -r requirements.txt`
2. **Google Cloud Configuration:**
   - Enable the **Gmail API** via the Google Cloud Console.
   - Generate **OAuth Desktop Credentials** and download `credentials.json`.
   - Ensure `credentials.json` is located in the project root directory.
3. **Execution:** Run `python sorter.py` to initiate the OAuth flow.

##  Security & Version Control
This project follows security best practices:
- **OAuth 2.0:** Secure authorization without storing user passwords.
- **Data Privacy:** `token.json` and `credentials.json` are strictly excluded from version control via `.gitignore`.
- **Scoped Access:** Minimal permissions (`gmail.modify`) used to ensure safe data interaction.

##  Result
The script successfully reduces manual email sorting time by approximately 90%, allowing for a focused primary inbox and structured archival of secondary communications.
