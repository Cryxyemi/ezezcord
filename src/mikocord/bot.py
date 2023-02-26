import os

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
        **kwargs
    ) -> None:
        super().__init__(Intents=intents, *args, **kwargs)

        self.token = token
        self.log_file = log_file
        self.__sync_commands = sync_commands
        self.ready_event = ready_print

        self.logger = Log(log_file=log_file, debug=debug)

        if self.__sync_commands:
            self.add_listener(self.__sync_cmds__, "on_connect")

    async def __sync_cmds__(self) -> None:
        self.logger.logger("Syncing slash commands", "mikocord", "info")
        await self.sync_commands()

    async def __connected__(self) -> None:
        self.logger.logger(f"Connected to Discord Gateway ({round(self.latency * 1000)}ms)", "mikocord", "info")

    async def __ready__(self) -> None:
        if self.ready_event:
            self.logger.logger("Bot is ready", "mikocord", "info")

    def exec(self) -> None:
        self.logger.logger("Starting bot", "mikocord", "info")
        self.run(self.token)

    def _register_cog(self, dir: str, subdir: str = None) -> None:
        self.logger.logger(f"Loading directory {dir}", "mikocord", "info")

        if not subdir:
            for file in os.scandir(dir):
                if file.endswith(".py"):
                    self.load_extension(f"{dir}.{file[:-3]}")
                    self.logger.logger(f"Loaded extension {dir}.{file[:-3]}", "mikocord", "info")
        else:
            for file in os.scandir(dir):
                if file.endswith(".py"):
                    self.load_extension(f"{dir}.{subdir}.{file[:-3]}")
                    self.logger.logger(f"Loaded extension {dir}.{subdir}.{file[:-3]}", "mikocord", "info")

    def load_dir(self, dir: str) -> None:
        self.logger.logger(f"Loading directory {dir}", "mikocord", "info")
        self._register_cog(dir)

    def load_subdir(self, dir: str) -> None:
        self.logger.logger(f"Loading subdirectory {dir}", "mikocord", "info")

        for subdir in os.scandir(dir):
            if subdir.is_dir():
                self._register_cog(dir, subdir.name)
