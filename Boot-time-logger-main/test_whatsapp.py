from twilio.rest import Client

account_sid = 'AC5cb4407ae5280663d545b3eb30af7470'
auth_token = '6c81ed3bd5991688b7fd139774a519c4'
client = Client(account_sid, auth_token)

from_whatsapp = 'whatsapp:+14155238886'
to_whatsapp = 'whatsapp:+918374572979'

message = client.messages.create(
    body='This is a test WhatsApp message from Python.',
    from_=from_whatsapp,
    to=to_whatsapp
)

print(f'Message sent: {message.sid}')
