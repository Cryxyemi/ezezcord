import discord
import mikocord as mc

bot = mc.Bot(
    intents=discord.Intents.default()
)

if __name__ == "__main__":
    bot.load_cogs("cogs")
    bot.run()
