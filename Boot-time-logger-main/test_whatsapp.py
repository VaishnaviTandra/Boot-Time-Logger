# send_whatsapp.py
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

# Get Twilio credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# WhatsApp sender and recipient
from_whatsapp = 'whatsapp:+14155238886'
to_whatsapp = 'whatsapp:+918374572979'

if not account_sid or not auth_token:
    raise ValueError("Twilio credentials not set in environment variables.")

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send message
message = client.messages.create(
    body='This is a test WhatsApp message from Python.',
    from_=from_whatsapp,
    to=to_whatsapp
)

print(f'Message sent: {message.sid}')
