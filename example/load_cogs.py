import mikocord as mc


bot = mc.Bot()

if __name__ == "__main__":
    bot.load_cogs("cogs")  # Load all cogs in the "cogs" folder
    # Load all cogs in the "commands" folder and all subfolders
    bot.load_cogs("commands", subdirectory=True)

    bot.run("token")  # Start the bot
