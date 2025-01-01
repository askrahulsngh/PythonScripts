import pywhatkit as kit
import csv

def send_whatsapp_message(to_number,nick_name, message):
    try:
        kit.sendwhatmsg_instantly(to_number, message, 10, True
        )
        print(f"Message sent to {nick_name}")
    except Exception as e:
        print(f"Failed to send message to {to_number}: {e}")

def send_messages_to_contacts(contacts, message):
    for phone_number, nick_name in contacts:
        custom_message = f"Hi {nick_name}, {message}"
        phone_number = phone_number.replace(" ", "")
        send_whatsapp_message(phone_number, nick_name, custom_message)

def read_contacts_from_csv(file_path):
    contacts = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                contacts.append((row['phone_number'], row['nick_name']))
    except Exception as e:
        print(f"Failed to read contacts from {file_path}: {e}")
    return contacts

if __name__ == "__main__":
    contacts = read_contacts_from_csv('contacts.csv')
    message = "\nMay 2025 be a year of prosperity, laughter, and unforgettable moments for you and your loved ones. \n -Rahul "

    send_messages_to_contacts(contacts, message)