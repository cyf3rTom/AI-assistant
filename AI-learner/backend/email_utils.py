#email_utils.py

# notifications/weekly_reminder.py
import os
import logging
import schedule
import time
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from dotenv import load_dotenv
# from app import app 
# from main import main

# -------------------- Setup Logging -------------------- #
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# # -------------------- Load Environment Files -------------------- #
# load_paths = []
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# for fname in ('.env', 'key.env'):
#     path = os.path.join(project_root, fname)
#     if os.path.isfile(path):
#         load_paths.append(path)

# if not load_paths:
#     logger.error("No .env or key.env found in %s", project_root)
#     raise FileNotFoundError("Environment file missing")

# for path in load_paths:
#     load_dotenv(path)
#     logger.info(f"Loaded environment from {os.path.basename(path)}")

# -------------------- SMTP Configuration -------------------- #
GEMINI_API_KEY="AIzaSyByJMZMXlIy7gU4siblYkI0I7AjrnJxxxx"
SMTP_HOST="smtp.gmail.com"
SMTP_PORT="587"
SMTP_USER="yashpawar.py@gmail.com"
SMTP_PASS="xxyashxx"
RECIPIENT_EMAIL="sha94@gmail.com"

# def get_smtp_config():
#     host = "smtp.gmail.com"   #os.getenv('SMTP_HOST')
#     user = "rgadhave8555@gmail.com"#os.getenv('SMTP_USER')
#     passwd = "ycqamfbhxzrjinhl"#os.getenv('SMTP_PASS')
#     recipient = email #"cybertom66@gmail.com"#os.getenv('RECIPIENT_EMAIL')
#     port = int("587")#int(os.getenv('SMTP_PORT', '587'))

#     # missing = [v for v in ('SMTP_HOST', 'SMTP_USER', 'SMTP_PASS', 'RECIPIENT_EMAIL') if not os.getenv(v)]
#     # if missing:
#     #     logger.error("Missing essential SMTP configurations: %s", ", ".join(missing))
#     #     raise SystemExit(1)

#     return host, port, user, passwd, recipient

# SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, RECIPIENT_EMAIL = get_smtp_config()
# TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates', 'weekly_syllabus_reminder.html')

# -------------------- Send Weekly Email -------------------- #


def send_weekly_mail(email, segment, retries=3, debug=0):
    subject = "Your Weekly Syllabus Completion Reminder"

    host = "smtp.gmail.com"
    user = "rgadhave8555@gmail.com"
    passwd = "ycqamfbhxzrjinhl"
    recipient = email #"cybertom66@gmail.com"   # Email passed from main.py
    port = 587

    TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), 'templates', 'weekly_syllabus_reminder.html')

    try:
        with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        html = f"<p>Reminder: {segment}</p>"

    text = f"Reminder: {segment}"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = recipient
    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))

    for attempt in range(1, retries + 1):
        try:
            with smtplib.SMTP(host, port, timeout=10) as server:
                server.starttls()
                server.login(user, passwd)
                server.send_message(msg)
                logger.info("Weekly reminder sent to %s", recipient)
                return
        except Exception as e:
            logger.error("Attempt %d/%d failed: %s", attempt, retries, e, exc_info=True)
            time.sleep(5)

    logger.error("All %d attempts to send email failed.", retries)




# def send_weekly_mail(retries=3):
#     """Read HTML template and send the weekly syllabus reminder with retry logic."""
#     subject = "Your Weekly Syllabus Completion Reminder"

#     try:
#         with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
#             html = f.read()
#     except FileNotFoundError:
#         html = "<p>Reminder: Keep tracking your syllabus progress.</p>"

#     text = "Reminder: Keep tracking your syllabus progress."

#     msg = MIMEMultipart("alternative")
#     msg["Subject"] = subject
#     msg["From"] = SMTP_USER
#     msg["To"] = RECIPIENT_EMAIL
#     msg.attach(MIMEText(text, "plain"))
#     msg.attach(MIMEText(html, "html"))

#     for attempt in range(1, retries + 1):
#         try:
#             with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as server:
#                 server.starttls()
#                 server.login(SMTP_USER, SMTP_PASS)
#                 server.send_message(msg)
#                 logger.info("Weekly reminder sent to %s", RECIPIENT_EMAIL)
#                 return
#         except Exception as e:
#             logger.error("Attempt %d/%d failed: %s", attempt, retries, e, exc_info=True)
#             time.sleep(5)

#     logger.error("All %d attempts to send email failed.", retries)

# -------------------- Scheduler Function -------------------- #
def run_scheduler():
    schedule.clear()
    # For production: schedule.every().monday.at("09:00").do(send_weekly_email)
    schedule.every(5).seconds.do(send_weekly_mail)
    logger.info("Scheduler initialized: sending test reminder every 5 seconds.")

    while True:
        schedule.run_pending()
        time.sleep(1)

# -------------------- Run Scheduler in Background -------------------- #
if __name__ == '__main__':
    t = threading.Thread(target=run_scheduler, daemon=True)
    t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Scheduler stopped by user.")
        raise SystemExit(0)
