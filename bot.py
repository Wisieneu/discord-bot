import discord
import responses

async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot(TOKEN):
    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('{} has been turned on successfully.\n'.format(client.user))
    
    # Logging every message the bot is able to see (if not sent by the bot itself)
    @client.event
    async def on_message(message):
        if message.author != client.user:
            username = str(message.author)
            user_message = str(message.content)
            channel = str(message.channel)

            print('{} ==> #{}\n{}: "{}"\n'.format(message.guild.name, channel, username, user_message))
            await send_message(message, user_message)

    client.run(TOKEN)