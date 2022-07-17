def append_reference_links( references: MemberReference) -> str:
    pass


def offender_found(member_name: str, entries_found: int, references: MemberReference) -> str:
    message_content: str = (
        f"""Member: {member_name} was found to have {entries_found} entries\n""",
    ) + append_reference_links(references)

    return message_content
