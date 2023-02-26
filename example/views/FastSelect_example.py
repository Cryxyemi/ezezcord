import discord
import mikocord as mc
from mikocord.modules import FastSelect


bot = mc.Bot(
    token="token"
)

@bot.slash_command()
async def test(ctx: discord.ApplicationContext):
    async def callback(interaction: discord.Interaction):
        if interaction.data["values"][0] == "test":
            await interaction.response.send_message("Test")
        elif interaction.data["values"][0] == "test2":
            await interaction.response.send_message("Test2")
        elif interaction.data["values"][0] == "test3":
            await interaction.response.send_message("Test3")
        else:
            await interaction.response.send_message("Error")

    select = FastSelect(
        callback=callback,
        placeholder="Test",
        min_values=1,
        max_values=1,
        row=0
    )
    select.add_option(label="Test", value="test")
    select.add_option(label="Test2", value="test2")
    select.add_option(label="Test3", value="test3")

    view = select.create_view()

    await ctx.respond("Message", view=view)


if __name__ == "__main__":
    bot.exec()