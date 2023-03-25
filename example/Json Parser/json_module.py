import discord
import mikocord as mc
from mikocord.ext import JsonParser

bot = mc.Bot()
reader = JsonParser("test.json")


@bot.slash_command(name="test")
async def test(ctx: discord.ApplicationContext) -> None:
    await ctx.respond(reader.get("test"))
    await ctx.send(reader.get("age"))

if __name__ == "__main__":
    bot.run("token")
