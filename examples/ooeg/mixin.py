class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add email logic here


class EmailableContact(Contact, MailSender):  # multiple inheritance
    pass


e = EmailableContact("John Smith", "jsmith@ex.net")
Contact.all_contacts
e.send_mail("Hello, test email here.")
