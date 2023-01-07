import requests
import json

def get_response(message) -> str:
    message_content = message.content.lower()
    
    # this checks whether the message is a command 
    if message_content[:2] == 'm!':
        message_content = message_content[2:]
        # joke command: returns a random joke taken from this API below
        if message_content == 'joke':
            response = requests.get(r"https://official-joke-api.appspot.com/random_joke")
            joke = json.loads(response.text)
            return f"{joke['setup']}\n\n...{joke['punchline']}"
        elif message_content == 'help':
            return '''```m!help -> Prints this page\nm!joke -> Prints a random joke (taken from various APIs)\n...with more to come```'''

    # if message not recognized as a command, will search for keywords to respond to
    phrases_list = {
        'baller': 'https://cdn.discordapp.com/attachments/654594751433146378/1033767835199078431/41ce545e2c093bcbf4461c459b4f4dec.mp4',
        'beast': 'https://media.discordapp.net/attachments/1034298084076834869/1057939585050615848/mrbeast-ytpmv.gif',
    }
    for phrase in phrases_list.keys():
        if phrase in message_content:
            return phrases_list[phrase]