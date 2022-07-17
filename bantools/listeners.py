from discord import DMChannel
from discord.ext import commands
from discord.ext.commands import Bot, bot, Cog
from discord.ext.commands.context import Context


class DiscordChannelListener(commands.Cog):
    def __init__(self, coreBot: Bot, guildId: int, channelId: int) -> None:

        self.bot = coreBot
        self.guildId = guildId
        self.channelId = channelId

    async