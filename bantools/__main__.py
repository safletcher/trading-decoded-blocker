from discord.ext.commands import Bot
from bantools.listeners import DiscordChannelListener
from bantools.utils.environ_tools import getenv_var


def main():

    bantools = Bot(command_prefix="/")
    listenerCog = DiscordChannelListener(bantools, "new-joiners")
    bantools.add_cog(listenerCog)

    discord_api_key = getenv_var("API_KEY")

    bantools.run()


if __name__ == "__main__":
    main()
