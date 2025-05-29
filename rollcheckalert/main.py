import pandas as pd
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Load Excel workbook with 2 sheets
df_master = pd.read_excel("/workspaces/pythonprojects/rollcheckalert/students.xlsx", sheet_name="main")
df_attendance = pd.read_excel("/workspaces/pythonprojects/rollcheckalert/students.xlsx", sheet_name="attendance")

# remove spaces from column names
df_master.columns = df_master.columns.str.strip()
df_attendance.columns = df_attendance.columns.str.strip()

# Extract roll numbers as sets
rollnos_master = set(df_master["enrolno"])
rollnos_attendance = set(df_attendance["Unnamed: 1"])

# print(df_master.columns)
# print(df_attendance.columns)

# Find missing roll numbers
missing_rollnos = rollnos_master - rollnos_attendance

# Print to console (for debugging)
print("Missing Roll Numbers:", missing_rollnos)

# Function to send email notification
def send_email(missing):
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("RECEIVER_EMAIL")

    if not email or not password or not receiver:
        print("Please check your .env file for EMAIL, PASSWORD, and RECEIVER_EMAIL")
        return

    subject = "Missing Roll Numbers Detected"
    body = f"The following roll numbers are missing:\n{', '.join(map(str, missing))}"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email
    msg["To"] = receiver
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email, password)
            smtp.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

# Send email if missing roll numbers are found
if missing_rollnos:
    send_email(missing_rollnos)
else:
    print("No missing roll numbers.")