import requests
import random
import time
import os
from colorama import Fore

print(" ====================================")

author = "X"

print("===========================================")
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print("===========================================\n")

time.sleep(1)

channel_id = input("Masukkan ID channel: ")
waktu1 = int(input("Set Waktu Hapus Pesan: "))
waktu2 = int(input("Set Waktu Kirim Pesan: "))

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

# Read the list of messages from file
with open("pesan.txt", "r") as f:
    words = f.readlines()

# Read the bot authorization token from file
with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
    channel_id = channel_id.strip()

    # Prepare the message payload
    payload = {
        'content': random.choice(words).strip()
    }

    # Set the authorization header
    headers = {
        'Authorization': authorization
    }

    # Send the message to Discord channel
    r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)

    if r.status_code == 200:
        message = r.json()
        message_id = message['id']
        print(Fore.WHITE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])
        print(Fore.GREEN + f'Message sent successfully with ID: {message_id}')

        # Wait for the specified time to delete the message
        time.sleep(waktu1)

        # Delete the message by ID
        response = requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
        if response.status_code == 204:
            print(Fore.GREEN + f'Pesan dengan ID {message_id} berhasil dihapus')
        else:
            print(Fore.RED + f'Gagal menghapus pesan dengan ID {message_id}: {response.status_code}')

    else:
        print(Fore.RED + f'Gagal mengirim pesan: {r.status_code}')

    # Wait for the specified time before sending the next message
    time.sleep(waktu2)
