@commands.command(pass_context=True)
    async def play(self, ctx):

        @commands.command(pass_context=True)
        async def join(self, ctx):
            usr = ctx.message.author
            channel = usr.voice.voice_channel
            server = ctx.message.server
            voice_client = self.bot.voice_client_in(server)
            if not usr.voice_channel:
                await self.bot.say("Você deve estar em um canal de voz para executar esse comando")
            if self.bot.is_voice_connected(server):
                await voice_client.move_to(channel)
            else:
                await self.bot.join_voice_channel(channel)

        @commands.command(pass_context=True)
        async def leave(self, ctx):
            server = ctx.message.server
            voice_client = self.bot.voice_client_in(server)
            if self.bot.is_voice_connected(server):
                await voice_client.disconnect()
            else:
                await self.bot.say("Bot não pode sair, por favor entre com o bot para poder sair")

        @commands.command(pass_context=True)
        async def play(self, ctx, url):
            server = ctx.message.server
            voice_client = self.bot.voice_client_in(server)
            player = await voice_client.create_ytdl_player(url)
            players[server.id] = player
            player.start()
