import mikocord as mc
import discord


bot = mc.Bot()


@bot.slash_command(name="ping")
async def ping(ctx: discord.ApplicationContext) -> None:
    await ctx.respond("pong")

if __name__ == "__main__":
    bot.run("token")
