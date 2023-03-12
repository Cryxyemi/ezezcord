import os
import time
from typing import Union
import asyncio

import discord

from .utils.log import Log


class Bot(discord.Bot):
    def __init__(self,
        token: str,
        intents: discord.Intents = discord.Intents.default(),
        ready_print: bool = True,
        debug: bool = True,
        log_file: bool = False,
        sync_commands: bool = True,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(intents=intents, *args, **kwargs)

        self.token = token
        self.log_file = log_file
        self.__sync_commands = sync_commands
        self.ready_event = ready_print
        self._debug = debug

        self._start_time: Union[float, None] = None

        self.logger = Log(log_file=log_file, debug=debug)

        if self.__sync_commands:
            self.add_listener(self.__sync_cmds__, "on_connect")

        if self.ready_event:
            self.add_listener(self.__connected__, "on_connect")
            self.add_listener(self.__ready__, "on_ready")

    async def __sync_cmds__(self) -> None:
        if self._debug:
            self.logger.logger("Syncing slash commands", "mikocord", "debug")
        await self.sync_commands()

    async def __connected__(self) -> None:
        self.logger.logger(f"Connected to Discord Gateway ({round(self.latency * 1000)}ms)", "websocket", "info")

    async def __ready__(self) -> None:
        self.logger.logger(f"Bot is ready", "mikocord", "info")
        self.logger.logger(f"Guild(s): {len(self.guilds)}", "mikocord", "info")
        self.logger.logger(f"Mikocord version: 1.9.0 | Pycord version: {discord.__version__}", "mikocord", "debug")

    def exec(self) -> None:
        self._start_time = time.time()
        self.logger.logger("Starting bot...", "mikocord", "info")
        self.run(self.token)

    def _register_cog(self, dir: str, subdir: str = None) -> None:
        if not subdir:
            for file in os.scandir(dir):
                if file.name.endswith(".py"):
                    self.load_extension(f"{dir}.{file.name[:-3]}")
                    if self._debug:
                        self.logger.logger(f"Loaded extension {dir}.{file.name[:-3]}", "cogs", "debug")
        else:
            for file in os.scandir(f"{dir}/{subdir}"):
                if file.name.endswith(".py"):
                    self.load_extension(f"{dir}.{subdir}.{file.name[:-3]}")
                    if self._debug:
                        self.logger.logger(f"Loaded extension {dir}.{subdir}.{file.name[:-3]}", "cogs", "debug")

    def load_dir(self, dir: str) -> None:
        if self._debug:
            self.logger.logger(f"Loading directory {dir}", "cogs", "debug")
        self._register_cog(dir)

    def load_subdir(self, dir: str) -> None:
        if self._debug:
            self.logger.logger(f"Loading subdirectory {dir}", "cogs", "debug")
        for subdir in os.scandir(dir):
            if subdir.is_dir():
                self._register_cog(dir, subdir.name)

    @property
    def start_time(self) -> float:
        if self._start_time is None:
            return self.logger._force_logger("Bot is not running, start_time will be None", "mikocord", "error")

        return self._start_time
    
    @property
    def uptime(self) -> float:
        if self._start_time is None:
            return self.logger._force_logger("Bot is not running, uptime will be None", "mikocord", "error")
        
        return time.time() - self._start_time
