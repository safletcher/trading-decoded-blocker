from discord.ext.commands import Bot
from discord import TextChannel, Message
from dataclasses import dataclass
from typing import List

MAX_MESSAGE_FETCH = 1000


@dataclass
class DiscordChannelConnectorArgs:
    bot: Bot
    guildId: int
    channelId: int


@dataclass
class MessageContent:
    messageId: int
    messageText: str


def to_generic_message(messages=List[Message]) -> List[MessageContent]:

    for message in messages:
        MessageContent(message.id, message.content)


class DiscordChannelConnector:
    def __init__(self, args: DiscordChannelConnectorArgs) -> None:

        self.coreBot: Bot = args.bot
        self.guildId: int = args.guildId

    async def fetch_messages(
        self, channelId: int, rowlimit: init = MAX_MESSAGE_FETCH
    ) -> None:

        if rowlimit > MAX_MESSAGE_FETCH:

            channel: TextChannel = self.bot.get_channel(channelId)
            messages: List[Message] = await channel.history(limit=rowlimit).flatten()

            generic_msg = to_generic_messages(messages)

            return generic_msg

    async def fetch_message_iterable(channelId: int) -> None:
        pass


def factory_get_channel(connectorArgs: DiscordChannelConnectorArgs):
    return DiscordChannelConnector(connectorArgs)
