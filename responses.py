import random
import requests
import json

def get_response(message: str) -> str:
    message = message.lower()
    
    # this checks whether the message is a command 
    if message[:2] == 'm!':
        message = message[2:]
        if message == 'joke':
            response = requests.get(r"https://official-joke-api.appspot.com/random_joke")
            tt = json.loads(response.text)
            return f"{tt['setup']}\n{tt['punchline']}"


    phrases_list = {
        'baller': 'https://cdn.discordapp.com/attachments/654594751433146378/1033767835199078431/41ce545e2c093bcbf4461c459b4f4dec.mp4',
        'beast': 'https://images-ext-1.discordapp.net/external/rgJ32du_uD-2yeC6gmKyjRZACFPZjBgOBY1bm-_eGXg/https/media.tenor.com/IIXy6CqR5l8AAAPo/mrbeast-ytpmv.mp4'
    }

    for phrase in phrases_list.keys():
        if phrase in message:
            return phrases_list[phrase]