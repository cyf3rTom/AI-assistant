import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

def send_email(emailId, data, debug=0):
    # SMTP Configuration - Replace with your own SMTP credentials
    smtpServer = 'smtp.gmail.com'
    smtpPort = 587
    senderEmail = 'yashpawar.py@gmail.com'
    senderPassword = 'email_password'  # Replace with secure method

    subject = f"Study Bot Content - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    message = MIMEMultipart()
    message['From'] = senderEmail
    message['To'] = emailId
    message['Subject'] = subject
    message.attach(MIMEText(data, 'plain'))

    if debug >= 1:
        print("AI_001:send_email - Function started")
        print(f"AI_002:send_email - Recipient = {emailId}")
        print(f"AI_003:send_email - Subject = {subject}")

    if debug >= 2:
        print(f"AI_004:send_email - Message content:\n{data}")

    try:
        server = smtplib.SMTP(smtpServer, smtpPort)
        server.starttls()

        if debug >= 2:
            print("AI_005:send_email - Connected to SMTP server, starting TLS")

        server.login(senderEmail, senderPassword)

        if debug >= 2:
            print("AI_006:send_email - Logged in to SMTP server")

        server.sendmail(senderEmail, emailId, message.as_string())

        if debug >= 1:
            print("AI_007:send_email - Email sent successfully")

        server.quit()

    except Exception as error:
        print("AI_008:send_email - Error occurred while sending email:")
        print(str(error))

