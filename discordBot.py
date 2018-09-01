import discord
import youtube_dl
from discord.ext import commands

bot = commands.Bot(command_prefix="_")
TOKEN = "NDgwODk3NTQxNDg0MDUyNDkw.DlufKQ.VpCKFfYi2zqHrWT50f-P-RLxA7w"
extensions = ['events', 'common', 'music']


@bot.event
async def on_ready():
    print("Sayuri reporting for duty")

if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print("Extensão {} carregada com sucesso".format(extension))
        except Exception as error:
            print("Extensão {} não foi carregada com sucesso. [{}]".format(extension, error))
    bot.run(TOKEN)
