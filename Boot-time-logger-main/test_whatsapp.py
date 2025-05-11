import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load credentials from .env file
load_dotenv()

# Get Twilio credentials and numbers from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_whatsapp = os.getenv('FROM_WHATSAPP')
to_whatsapp = os.getenv('TO_WHATSAPP')

# Validate credentials
if not all([account_sid, auth_token, from_whatsapp, to_whatsapp]):
    raise ValueError("❌ Twilio credentials or phone numbers not set properly in .env")

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Send message
try:
    message = client.messages.create(
        body='📢 This is a test WhatsApp message from Python.',
        from_=from_whatsapp,
        to=to_whatsapp
    )
    print(f"✅ Message sent successfully! SID: {message.sid}")
except Exception as e:
    print(f"❌ Failed to send WhatsApp message: {e}")
