import discord
import youtube_dl
from discord.ext import commands
from random import randint

bot = commands.Bot(command_prefix="_")
TOKEN = "NDgwODk3NTQxNDg0MDUyNDkw.DlufKQ.VpCKFfYi2zqHrWT50f-P-RLxA7w"
players = {}


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Diga _help'))
    print("Sayuri reporting for duty")


@bot.command(pass_context=True)
async def greet(ctx):
    def switch(num):
        greetings = {
            0: "Eae ",
            1: "Yo ",
            3: "Sup ",
            4: "Whassup ",
            5: "Fala tu ",
            6: "Oim ",
            7: "Oi lindo ",
            8: "Quer oq? ",
            9: "Fala porra "
        }
        return greetings.get(num, "Late ")

    usr = ctx.message.author.id
    greetnum = randint(0, 9)
    greeting = switch(greetnum)

    await bot.say(greeting + "<@%s>" % usr)


@bot.command()
async def ping():
    await bot.say("Pong")


@bot.command()
async def echo(*args):
    output = ''
    for x in args:
        output += x
        output += ' '
    await bot.say(output)


@bot.command(pass_context=True)
async def join(ctx):
    usr = ctx.message.author
    channel = usr.voice.voice_channel
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    if not usr.voice_channel:
        await bot.say("Você deve estar em um canal de voz para executar esse comando")
    if bot.is_voice_connected(server):
        await voice_client.move_to(channel)
    else:
        await bot.join_voice_channel(channel)


@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    if bot.is_voice_connected(server):
        await voice_client.disconnect()
    else:
        await bot.say("Bot não pode sair, por favor entre com o bot para poder sair")


@bot.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

bot.run(TOKEN)