import os
from typing import Literal

from colorama import Fore

from .times import get_date


class Log:
    """A logger class that logs messages to the console and/or a log file."""

    def __init__(self,
                 log_file: bool = False,
                 debug: bool = True,
                 with_date: bool = True
                 ) -> None:
        self.log_file = log_file
        self.debug = debug
        self.date = with_date

        self.warned = False

    def _force_logger(self, message: str, module: str, level: Literal["info", "warning", "error", "debug"] = "info") -> None:
        """Not ment to be used by the user."""
        if self.date:
            print(self._color_string(
                f"[{level.upper()} | {get_date()}] [{module}] {message}", level))
        else:
            print(self._color_string(
                f"[{level.upper()}] [{module}] {message}", level))

    def logger(self, message: str, module: str, level: Literal["info", "warning", "error", "debug"] = "info") -> None:
        """Logs a message to the console and/or a log file.

        It should look like this:
        `[LEVEL | DATE] [MODULE] [MESSAGE]`

        Args
        ----
        message: `str`
            The message to log.
        module: `str`
            The module that the message is from.
        level: `Literal["info", "warning", "error", "debug"]`
            The level of the message. Defaults to "info".

        Returns
        -------
        None
        """
        if self.log_file and self.debug:
            if not os.path.exists("logs"):
                os.mkdir("logs")

            with open("logs/debug.log", "a") as f:
                if self.date:
                    f.write(
                        f"[{level.upper()} | {get_date()}] [{module}] {message}\n")
                else:
                    f.write(f"[{level.upper()}] [{module}] {message}\n")
        elif self.debug and not self.log_file:
            if self.date:
                print(self._color_string(
                    f"[{level.upper()} | {get_date()}] [{module}] {message}", level))
            else:
                print(self._color_string(
                    f"[{level.upper()}] [{module}] {message}", level))
        elif not self.debug and self.log_file:
            if not self.warned:
                print(self._color_string(
                    f"[WARNING | {get_date()}] [MIKOCORD] Debug is disabled, but log file is enabled. Please disable log file or enable debug.", "error"))
                self.warned = True
        else:
            pass

    def _color_string(self, string: str, level: Literal["info", "warning", "error", "debug"]) -> str:
        """Not ment to be used by the user."""
        if level == "info":
            return f"{Fore.GREEN}{string}{Fore.RESET}"
        elif level == "warning":
            return f"{Fore.YELLOW}{string}{Fore.RESET}"
        elif level == "error":
            return f"{Fore.RED}{string}{Fore.RESET}"
        elif level == "debug":
            return f"{Fore.CYAN}{string}{Fore.RESET}"
        else:
            return string
