from email.message import EmailMessage

import smtplib
import ssl

# Setup port number and server name

smtp_port = 587  # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

emails = ['email 1', 'email 2']
websites = ['microsoft.com', 'apple.com']
companies = ['Microsoft', 'Apple']

email_from = "your email"
email_to = emails

pswd = "___________"

# content of message

subject = 'subject'
message = 'message'

em = EmailMessage()
em['subject'] = subject
em.set_content(message)

# Create context

simple_email_context = ssl.create_default_context()

try:
    # Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")

    # Send the actual email
    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, em.as_string())
    print(f"Email successfully sent to - {email_to}")

# If there's an error, print it out
except Exception as e:
    print(e)

# Close the port
finally:
    TIE_server.quit()



























