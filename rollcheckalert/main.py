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
rollnos_attendance = set(df_attendance["enrolno"])

print(df_master)

