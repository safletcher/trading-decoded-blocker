from discord.member import Member
from bantools.cqrs.discord import get_member_reference_in_channel


def find_duplicate_users_usecase(member: Member) -> None:

    messages = get_member_reference_in_channel(member.display_name)

