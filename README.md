# Telescrape

Telescrape is a Python-based tool that scrapes `.txt` files from Telegram channels. It utilizes the Telethon library for seamless interaction with the Telegram API. The tool is configurable via a `config.json` file, allowing users to customize API details and specify target channels.

## Features
- Scrapes `.txt` files from specified Telegram channels.
- Uses a `config.json` file for API credentials and channel links.
- Ensures files are not duplicated by checking existing file sizes.
- Displays a loading animation and status updates.
- Works on both Windows and Linux.

## Requirements
- Python 3.7+
- Telethon
- Colorama

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/telescrape.git
   cd telescrape
   ```
2. Install dependencies:
   ```bash
   pip install telethon colorama
   ```
3. Inside the `config.json` file in the project directory:
   ```json
   {
     "api_id": YOUR_API_ID,
     "api_hash": "YOUR_API_HASH",
     "channels": ["https://t.me/yourchannel"]
   }
   ```

## Usage
1. Run the script:
   ```bash
   python telescrape.py
   ```
2. Enter the output directory where files should be saved.
3. The script will connect to Telegram and start scraping files from the specified channels.

## Example Output
```
[+] Connecting to Telegram...
[+] Connected!
[+] Scraping channel: https://t.me/yourchannel
[+] Downloading: output/example.txt
[+] Saved: output/example.txt
[+] Done scraping.
```

## Troubleshooting
- Ensure your `config.json` file is correctly formatted and contains valid API credentials.
- Check if you have access to the specified Telegram channels.
- If encountering issues, try deleting the `session.session` file and restarting the script.

## Disclaimer
This tool is intended for educational and personal use only. Ensure that you have permission to scrape data from the specified channels.
Please Star This Repo :D

