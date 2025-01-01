from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER

def send_whatsapp_message(to_number, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            body=message,
            from_=f'whatsapp:{TWILIO_WHATSAPP_NUMBER}',
            to=f'whatsapp:{to_number}'
        )
        print(f"Message sent to {to_number}")
    except Exception as e:
        print(f"Failed to send message to {to_number}: {e}")

def send_messages_to_contacts(contacts, message):
    for contact in contacts:
        send_whatsapp_message(contact, message)

if __name__ == "__main__":
    contacts = ["+12345678901", "+10987654321"]
    message = "This is a test message."

    send_messages_to_contacts(contacts, message)