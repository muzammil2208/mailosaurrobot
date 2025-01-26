from mailosaur.models import SearchCriteria
import mailosaur
from pprint import pprint 

class MailosaurLibrary:
    """
    A Python library to retrieve the last received email using the Mailosaur API.
    """

    def __init__(self, api_key, server_id):
        """
        Initialize the MailosaurLibrary with the API key and server ID.

        Arguments:
        - `api_key`: Your Mailosaur API key.
        - `server_id`: The Mailosaur server ID.
        """
        self.client = mailosaur.MailosaurClient(api_key)
        self.server_id = server_id
        print("MailosaurLibrary initialized")

    def get_last_email(self, sent_from, timeout=30):
        """
        Retrieve the last email sent from a specific email address.

        Arguments:
        - `sent_from`: The email address to filter by.
        - `timeout`: Time (in seconds) to wait for an email (default is 30 seconds).

        Returns:
        - A dictionary with the email's subject, body, sender, and received time.
        """
        # Define the search criteria
        criteria = SearchCriteria()
        criteria.sent_from=sent_from


       
        # Use the search method to find emails
        try:    
            emails =self.client.messages.search(self.server_id,criteria) 
            if emails.items:
                    email = emails.items[0]  # Get the first email
                    print("Subject:", email.subject)
                    print("Body:", email.summary)
                    print("-" * 50)
                    return {
                        "subject": email.subject,
                        "body": email.summary,
                    }
            else:
                    print("No emails found from the specified sender.")
                    return None
        except Exception as e:
            print("An error occurred:", str(e))
            return None
      
