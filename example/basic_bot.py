import mikocord as mc
import discord


bot = mc.Bot(
    token="token"
)

@bot.slash_command(name="ping")
async def ping(ctx: discord.ApplicationContext) -> None:
    await ctx.respond("pong")

if __name__ == "__main__":
    bot.load_cogs("cogs")  # Load all cogs in the "cogs" folder
    bot.load_subdir("commands")  # Load all cogs in the "commands" folder and all subfolders

    bot.exec()
