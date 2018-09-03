import discord
from discord.ext import commands
from random import randint
players = {}


class Commands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def greet(self, ctx):
        def switch(num):
            greetings = {

            }
            return greetings.get(num, " ")

        usr = ctx.message.author.id
        greetnum = randint(0, 9)
        greeting = switch(greetnum)

        await self.bot.say(greeting + "<@%s>" % usr)

    @commands.command()
    async def ping(self):
        await self.bot.say("Pong")

    @commands.command()
    async def echo(self, *args):
        output = ''
        for x in args:
            output += x
            output += ' '
        await self.bot.say(output)




def setup(bot):
    bot.add_cog(Commands(bot))