import mikocord as mc
from mikocord.modules import ModalIO


bot = mc.Bot(
    token="token",
    debug=True,
)

@bot.command()
async def test(ctx) -> None:
    model = ModalIO("Test")
    model.app_option("Cool label", "Ghost placeholder")
    result = await model.send_wait(ctx)
    if result is not None:
        await ctx.send(", ".join([i.value for i in result]))
    else:
        await ctx.send("Something went wrong :/")

if __name__ == "__main__":
    bot.exec()
