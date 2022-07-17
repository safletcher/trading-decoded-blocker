from discord.ext.commands import Bot
from listeners import DiscordChannelListener
from utils.environ_tools import getenv_var


def main():

    bantools = Bot(command_prefix="/")
    listenerCog = DiscordChannelListener(bantools, "new-joiners")
    bantools.add_cog(listenerCog)

    discord_api_key = getenv_var("API_KEY")

    print(f"discord_api_key = {discord_api_key}")
    # bantools.run()


if __name__ == "__main__":
    main()
