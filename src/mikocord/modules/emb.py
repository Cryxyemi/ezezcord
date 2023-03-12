"""Embed templates that can be used to send messages to users.
These functions will generate embeds and send them as an ephemeral message to the user.

Example
-------
.. code-block:: python

    from ezcord import Bot, Embeds

    bot = Bot()

    @bot.slash_command()
    async def hey(ctx):
        await emb.success(ctx, "Success!")
"""

from typing import Union

import discord
from discord import Color


class Embeds:
    """Embed templates.
    
    Private methods
    ---------------
    ``__send_embed__`` -> Sends an Embed.

    Public methods
    --------------
    ``error`` -> Sends an error message.

    ``success`` -> Sends a success message.

    ``info`` -> Sends an info message.
    
    ``warn`` -> Sends a warning message.
    """
    @classmethod
    async def __send_embed__(
        cls,
        ctx: Union[discord.ApplicationContext, discord.Interaction],
        embed: discord.Embed,
        view: discord.ui.View = None
    ):
        if view is None:
            try:
                await ctx.response.send_message(embed=embed, ephemeral=True)
            except discord.InteractionResponded:
                await ctx.followup.send(embed=embed, ephemeral=True)
        else:
            try:
                await ctx.response.send_message(embed=embed, ephemeral=True, view=view)
            except discord.InteractionResponded:
                await ctx.followup.send(embed=embed, ephemeral=True, view=view)

    @classmethod
    async def error(
        cls,
        ctx: Union[discord.ApplicationContext, discord.Interaction],
        txt: str,
        view: discord.ui.View = None
    ):
        """Send an error message.

        Parameters
        ----------
        ctx:
            The application context or the interaction to send the message to.
        txt:
            The text to send.
        view:
            The view to send with the message.

        """
        embed = discord.Embed(
            description=txt,
            color=Color.red()
        )
        await cls.__send_embed__(ctx, embed, view)

    @classmethod
    async def success(
        cls,
        ctx: Union[discord.ApplicationContext, discord.Interaction],
        txt: str,
        view: discord.ui.View = None
    ):
        """Send a success message.

        Parameters
        ----------
        ctx:
            The application context or the interaction to send the message to.
        txt:
            The text to send.
        view:
            The view to send with the message.

        """
        embed = discord.Embed(
            description=txt,
            color=Color.green()
        )
        await cls.__send_embed__(ctx, embed, view)

    @classmethod
    async def info(
        cls,
        ctx: Union[discord.ApplicationContext, discord.Interaction],
        txt: str,
        view: discord.ui.View = None
    ):
        """Send an info message.

        Parameters
        ----------
        ctx:
            The application context or the interaction to send the message to.
        txt:
            The text to send.
        view:
            The view to send with the message.

        """
        embed = discord.Embed(
            description=txt,
            color=Color.blue()
        )
        await cls.__send_embed__(ctx, embed, view)

    @classmethod
    async def warn(
        cls,
        ctx: Union[discord.ApplicationContext, discord.Interaction],
        txt: str,
        view: discord.ui.View = None
    ):
        """Send a warning message.

        Parameters
        ----------
        ctx:
            The application context or the interaction to send the message to.
        txt:
            The text to send.
        view:
            The view to send with the message.

        """
        embed = discord.Embed(
            description=txt,
            color=Color.orange()
        )
        await cls.__send_embed__(ctx, embed, view)
