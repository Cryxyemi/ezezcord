from enum import Enum
from typing import Union

import discord
from discord.ui import Modal
from discord import InputText, InputTextStyle

from ..utils.times import Convertor
from ..utils.log import Log


class InputStyle(Enum):
    ONE_LINE = InputTextStyle.short
    MULTI_LINE = InputTextStyle.long
    PARAGRAPH = InputTextStyle.paragraph


class ModalIO(Modal):
    def __init__(
        self,
        title: str
    ) -> None:
        self.con = Convertor()
        self.log = Log(debug=False, with_date=False)

        super().__init__(title=title, custom_id="MODALIO", timeout=self.con.from_minute(10))

    def app_option(
        self,
        label: str,
        placeholder: str,
        style: InputStyle = InputStyle.ONE_LINE
    ) -> None:
        self.add_item(InputText(
            label=label,
            placeholder=placeholder,
            style=style,
        ))

    async def send_wait(
        self,
        ctx: Union[discord.ApplicationContext, discord.Interaction]
    ):
        try:
            if type(ctx) == discord.ApplicationContext:
                await ctx.send_modal(self)
            else:
                await ctx.response.send_modal(self)
            await self.wait()
            return self.children
        except:
            return self.log._force_logger("Make sure you dont responded to the interaction before sending the modal.", "ModalIO", "error")
        
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()
