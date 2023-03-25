import asyncio
import discord
import mikocord as mc
from mikocord import execute, FetchTypes


bot = mc.Bot()

# Database module


@execute()
async def create_table() -> str:
    return "CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER)"


@execute()
async def insert_user(name: str, age: int) -> str:
    return "INSERT INTO users VALUES (?, ?)"


@execute(fetch=FetchTypes.ALL)
async def get_users() -> str:
    return "SELECT * FROM users"

# Database module


@bot.slash_command(name="add_user")
async def add_user(ctx: discord.ApplicationContext, name: str, age: int) -> None:
    await insert_user(name, age)
    await ctx.respond("User added")


@bot.slash_command(name="get_users")
async def get_users(ctx: mc.ApplicationContext) -> None:
    users = await get_users()
    await ctx.respond(users)


if __name__ == "__main__":
    asyncio.run(create_table())  # Create the table

    bot.run("token")  # Start the bot
