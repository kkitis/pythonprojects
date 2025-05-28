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

# Extract roll numbers as sets
rollnos_master = set(df_master["enrolno"])
rollnos_attendance = set(df_attendance["enrolno"])

# Find missing roll numbers
missing_rollnos = rollnos_master - rollnos_attendance

# Print to console (for debugging)
print("Missing Roll Numbers:", missing_rollnos)

