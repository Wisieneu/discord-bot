import bot
import os

if __name__ == '__main__':
    f = open('token.txt')
    bot_token = f.read(72)
    bot.run_discord_bot(bot_token)