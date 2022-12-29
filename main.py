import bot
import os

if __name__ == '__main__':
    # reads the token from a separate file (not shown here for obvious reasons)
    f = open('token.txt')
    bot_token = f.read(72)
    bot.run_discord_bot(bot_token)