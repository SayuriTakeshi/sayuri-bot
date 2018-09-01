import discord
from discord.ext import commands
import json


class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        filtro = ["BANANA", "APPLE"]

        content = message.content.split(" ")
        for word in content:
            if word.upper() in filtro:
                try:
                    await self.bot.delete_message(message)
                    await self.bot.send_message(message.channel, "No bad words in this server")
                except Exception as error:
                    return

    async def update_users(self, user):
        with open("users.json", "r") as f:
            users = json.load(f)

        if not user.id in users:
            users[user.id] = {}
            users[user.id]['strikes'] = 0
            users[user.id]['experience'] = 0
            users[user.id]['level'] = 1

        with open("users.json", "w") as f:
            json.dump(users, f)


def setup(bot):
    bot.add_cog(Events(bot))
