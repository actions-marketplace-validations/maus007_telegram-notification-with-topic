
import requests
import os, sys

def send_to_telegram(message):
    TOKEN = os.environ["IMPUT_TELEGRAM_TOKEN"]
    TO = os.environ["IMPUT_TELEGRAM_TO"]
    TOPIC = os.getenv("INPUT_TELEGRAM_TOPIC", default=None)
    apiURL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    parse_mode = os.getenv("INPUT_PARSE_MODE", default="markdown")

    if TOPIC != None:
        payload = {
            'chat_id': TO,
            'text': message,
            'message_thread_id': TOPIC,
            'parse_mode': parse_mode
        }
    else:
        payload = {
            'chat_id': TO,
            'text': message,
            'parse_mode': parse_mode
        }

    try:
        response = requests.post(apiURL, json=payload)
        print(response.text)
    except Exception as e:
        print(e)


send_to_telegram(os.environ["INPUT_MESSAGE"])