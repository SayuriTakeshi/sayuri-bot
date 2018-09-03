import discord
import requests
import urllib3
from discord.ext import commands
from bs4 import BeautifulSoup
from pprint import pprint
import re


embedPlayer = discord.Embed(
            title='SayuBOT  Player',
            description='Digite um numero entre 1 e 5',
            colour=0xe74c3c
        )


class Commands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def summon(self, ctx):
        usr = ctx.message.author
        channel = usr.voice.voice_channel
        server = ctx.message.channel
        voice_client = self.bot.voice_client_in(server)
        if not usr.voice_channel:
            await self.bot.say("Você deve primeiro se conectar ao canal de voz")
        elif self.bot.is_voice_connected(server):
            await voice_client.move_to(channel)
        else:
            await self.bot.join_voice_channel(channel)

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.message.server
        voice_client = self.bot.voice_client_in(server)
        if self.bot.is_voice_connected(server):
            await voice_client.disconnect()
        elif not self.bot.is_voice_connected(server):
            await self.bot.say("O bot deve estar conectado para poder usar esse comando")

    @commands.command()
    async def play(self,*args):
        url = "https://www.youtube.com/results?search_query=" + '+'.join(args)

        data = requests.get(url)
        data = data.text
        soup = BeautifulSoup(data, "html.parser")
        vids = soup.find_all(attrs={'class': 'yt-uix-tile-link'})
        duracao = soup.find_all(attrs={'class': 'accessible-description'})
        print(len(vids))
        lista = zip(vids[:5],duracao[:5])

        for x,y in lista:
            string = x['title'] + ' - '+ y.getText()[3:]
            if string[-1] == '.':
                string = string[:-1]

            await self.bot.say(string)

            #embedPlayer.add_field(name=vids[x]['title'], value='', inline=True)
        #await self.bot.say(embed=embedPlayer)
        #num = self.get_num()

    @commands.command()
    async def get_num(self, ctx):
        self.bot.say("Digite um numero de 1 a 5")
        num = ctx.message.content
        return num


def setup(bot):
    bot.add_cog(Commands(bot))