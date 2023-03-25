import os
import time
import json
import importlib.util
from typing import Union

import discord

from .utils.log import Log
from .errors import NoSetupFound

_version = "2.0.0"


class Bot(discord.Bot):
    """
    The main bot class

    Args
    ----
    intents: discord.Intents (optional) The intents to use
    *args: Any (optional) Any arguments to pass to the `discord.Client` class
    **kwargs: Any (optional) Any keyword arguments to pass to the `discord.Client` class

    Public Methods
    --------------
    `run(token: str = None)` -> None
        Starts the bot

    Public Variables
    ----------------
    `uptime`: float
        The uptime of the bot in seconds

    `start_time`: float
        The time the bot started in seconds

    Private Methods
    ---------------
    `_ignore_pycache(dir: str)` -> bool
        Checks if a directory is a pycache directory

    `_register_cog(dir: str, subdir: bool = None)` -> None
        Register a directory of cogs

    `_load_config()` -> None
        Loads the config file

    `_sync_cmds()` -> None
        Syncs the slash commands

    `_connected()` -> None
        Called when the bot connects to the gateway

    `_ready()` -> None
        Called when the bot is ready
    """

    def __init__(self,
                 intents: discord.Intents = discord.Intents.default(),
                 *args,
                 **kwargs,
                 ) -> None:
        self._load_config()

        super().__init__(intents=intents, *args, **kwargs)

        self.token: str = None
        self.log_file: bool = None
        self.__sync_commands: bool = None
        self.ready_event: bool = None
        self._debug: bool = None

        self._start_time: Union[float, None] = None

        self.logger = Log(log_file=self.log_file, debug=self._debug)

        if self.__sync_commands:
            self.add_listener(self._sync_cmds, "on_connect")

        if self.ready_event:
            self.add_listener(self._connected, "on_connect")
            self.add_listener(self._ready, "on_ready")

    async def _sync_cmds(self) -> None:
        """Not to be used by the user"""
        if self._debug:
            self.logger.logger("Syncing slash commands", "mikocord", "debug")
        await self.sync_commands()

    async def _connected(self) -> None:
        """Not to be used by the user"""
        self.logger.logger(
            f"Connected to Discord Gateway ({round(self.latency * 1000)}ms)", "websocket", "info")

    async def _ready(self) -> None:
        """Not to be used by the user"""
        self.logger.logger(f"Bot is ready", "mikocord", "info")
        self.logger.logger(f"Guild(s): {len(self.guilds)}", "mikocord", "info")
        self.logger.logger(
            f"Mikocord version: {_version} | Pycord version: {discord.__version__}", "mikocord", "debug")

    def run(self, token: str = None) -> None:
        """Starts the bot

        Args
        ----
        token: str (optional) If the token is not provided in the `config` file, you can provide it here"""

        if token:
            self.token = token
        self._start_time = time.time()
        self.logger.logger("Starting bot...", "mikocord", "info")
        super().run(self.token, reconnect=True)

    def _ignore_pycache(self, dir: str) -> bool:
        """Not ment to be used by the user. Checks if a directory is a pycache directory"""
        return "pycache" in dir

    def _register_cog(self, dir: str, subdir: bool = None) -> None:
        """Not to be used by the user. Register a directory of cogs"""
        if not subdir:
            for file in os.scandir(dir):
                if file.is_file():
                    name = file.name.split(os.path.sep)[0]

                    spec = importlib.util.spec_from_file_location(
                        name, file.path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    try:
                        module.setup(self)
                    except AttributeError:
                        raise NoSetupFound(module)
        else:
            for cog_dir in os.scandir(dir):
                if cog_dir.is_dir():
                    for subfile in os.scandir(cog_dir.path):
                        if subfile.is_file():
                            name = subfile.name.split(os.path.sep)[0]

                            spec = importlib.util.spec_from_file_location(
                                name, subfile.path)
                            module = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module)

                            try:
                                module.setup(self)
                            except AttributeError:
                                raise NoSetupFound(module)

    def load_cogs(self, *dirs: str, subdirectory: bool = False) -> None:
        """Loads cogs from a directory

        Args
        ----
        *dirs: str (required) The directories to load cogs from
        subdirectory: bool (optional) Whether to load cogs from subdirectories"""

        for dir in dirs:
            self._register_cog(dir, subdir=subdirectory)

    def _load_config(self) -> dict:
        """Not to be used by the user. Loads the config file"""
        self.logger.logger("Loading config file...", "mikocord", "debug")

        if not os.path.exists("mikocord.json"):
            with open("mikocord.json", "w") as f:
                json.dump({
                    "token": "",
                    "debug": True,
                    "log_file": False,
                    "sync_commands": True,
                    "ready_print": True,
                }, f, indent=4, ensure_ascii=False)

        with open("mikocord.json", "r") as f:
            config = json.load(f)

        if config["token"] != str:
            raise ValueError("Token must be a string")

        self.token = config["token"]

        if config["debug"] != bool:
            raise ValueError("Debug must be a boolean")

        self._debug = config["debug"]

        if config["log_file"] != bool:
            raise ValueError("Log file must be a boolean")

        self.log_file = config["log_file"]

        if config["sync_commands"] != bool:
            raise ValueError("Sync commands must be a boolean")

        self.__sync_commands = config["sync_commands"]

    @property
    def start_time(self) -> float:
        """Returns the time the bot started"""
        if self._start_time is None:
            return self.logger._force_logger("Bot is not running, start_time will be None", "mikocord", "error")

        return self._start_time

    @property
    def uptime(self) -> float:
        """Returns how long the bot is online"""
        if self._start_time is None:
            return self.logger._force_logger("Bot is not running, uptime will be None", "mikocord", "error")

        return time.time() - self._start_time
