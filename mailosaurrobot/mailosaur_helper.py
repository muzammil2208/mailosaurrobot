import mailosaur


class MailosaurLibrary:
    """
    A Robot Framework library to retrieve the last received email using the Mailosaur API.
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

    def get_last_email(self, sent_to, timeout=30):
        """
        Retrieve the last email sent to a specific email address.

        Arguments:
        - `sent_to`: The email address to filter by.
        - `timeout`: Time (in seconds) to wait for an email (default is 30 seconds).

        Returns:
        - A dictionary with the email's subject, body, sender, and received time.
        """
        criteria = {"sent_to": sent_to}
        email = self.client.messages.wait_for(self.server_id, criteria, timeout)

        return {
            "subject": email.subject,
            "body": email.text.body,
            "sender": email.from_email,
            "received_at": email.received,
        }

    def log_last_email(self, sent_to, timeout=30):
        """
        Retrieve the last email and log its details.

        Arguments:
        - `sent_to`: The email address to filter by.
        - `timeout`: Time (in seconds) to wait for an email (default is 30 seconds).
        """
        email_data = self.get_last_email(sent_to, timeout)
        print(f"Subject: {email_data['subject']}")
        print(f"Body: {email_data['body']}")
        print(f"Sender: {email_data['sender']}")
        print(f"Received At: {email_data['received_at']}")
