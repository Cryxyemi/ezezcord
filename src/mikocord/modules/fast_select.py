import discord


class FastSelect(discord.ui.Select):
    """A class to create fast a select menu."""
    def __init__(
            self,
            callback: callable,
            placeholder: str = None,
            custom_id: str = "ez_select",
            min_values: int = 1,
            max_values: int = 1,
            disabled: bool = False,
            row: int = None
        ) -> None:
        super().__init__(
            placeholder=placeholder,
            custom_id=custom_id,
            min_values=min_values,
            max_values=max_values,
            disabled=disabled,
            row=row
        )
    
        self.callback = callback

    def create_view(self, timeout: int = 180) -> discord.ui.View:
        view = discord.ui.View(timeout=timeout)
        view.add_item(self)
        return view

    async def callback(self, interaction: discord.Interaction):
        await self.callback(interaction)
