from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

from_whatsapp = ''
to_whatsapp = ''

message = client.messages.create(
    body='This is a test WhatsApp message from Python.',
    from_=from_whatsapp,
    to=to_whatsapp
)

print(f'Message sent: {message.sid}')
