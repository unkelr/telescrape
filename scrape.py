import json
import os
from telethon import TelegramClient
from colorama import Fore, Style
import sys
import time

red = Fore.RED
green = Fore.GREEN
dim = Style.DIM
bright = Style.BRIGHT
res = Style.RESET_ALL
re = Fore.RESET

def loadingscreen2():
    animation = [f"{green}[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.7)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()


def clearscrene():
    os.system('cls' if os.name == 'nt' else 'clear')

clearscrene()

if not os.path.exists("config.json"):
    print("Missing config.json! Please create it with API details and channel links.")
    exit(1)

with open("config.json", "r") as f:
    config = json.load(f)

API_ID = config["api_id"]
API_HASH = config["api_hash"]
SESSION_NAME = "session" 
CHANNELS = config["channels"]

if not CHANNELS:
    print("No channels specified in config.json!")
    exit(1)

SAVE_DIR = input(f"{green}[+]{re}{res} Output Files: ")
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def scrape_old_files():
    print(f"{green}[+]{re}{res} Connecting to Telegram... ")
    loadingscreen2()
    print("\n")
    await client.start()
    print(f"{green}[+]{re}{res} Connected!")
    time.sleep(0.5)
    clearscrene()
    for channel in CHANNELS:
        print(f"{green}[+]{re}{res} Scraping channel: {channel}")
        try:
            async for message in client.iter_messages(channel):
                if message.file and message.file.name.endswith(".txt"):
                    filename = os.path.join(SAVE_DIR, message.file.name)
                    file_size = message.file.size
                    
                    if os.path.exists(filename):
                        existing_file_size = os.path.getsize(filename)
                        if existing_file_size == file_size:
                            print(f"{red}[-]{re}{res} Skipping file: {filename}")
                            continue
                    
                    print(f"{green}[+]{re}{res} Downloading: {filename}")
                    await message.download_media(file=filename)
                    print(f"{green}[+]{re}{res} Saved: {filename}")
        except Exception as e:
            print(f"{red}[-]{re}{res} Error processing {channel}: {e}")
    
    print(f"{green}[+]{re}{res} Done scraping.")
    await client.disconnect()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(scrape_old_files())