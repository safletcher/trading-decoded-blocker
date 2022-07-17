from discord import Member
from dataclasses import dataclass
from discord.ext.commands import Bot

@dataclass
class GetMemberReferenceArgs:
    display_name: Member.diplay_name
    bot: Bot
    guildId: int
    channelId: int


def get_member_reference_in_channel(memberRefArgs : GetMemberReferenceArgs):
    pass

