import os
from typing import Literal
import warnings

from colorama import Fore, Style

from .times import get_date


class Log:
    def __init__(self,
        log_file: bool = False,
        debug: bool = True,
        with_date: bool = True
    ) -> None:
        self.log_file = log_file
        self.debug = debug
        self.date = with_date

        self.warned = False

    def logger(self, message: str, module: str, level: Literal["info", "warning", "error", "debug"] = "info") -> None:
        if self.log_file and self.debug:
            if not os.path.exists("logs"):
                os.mkdir("logs")

            with open("logs/debug.log", "a") as f:
                if self.date:
                    f.write(f"[{level.upper()} | {get_date()}] [{module}] {message}")
                else:
                    f.write(f"[{level.upper()}] [{module}] {message}")

        elif self.debug and not self.log_file:
            if self.date:
                print(f"[{level.upper()} | {get_date()}] [{module}] {message}")
            else:
                print(f"[{level.upper()}] [{module}] {message}")

        elif not self.debug and self.log_file:
            if not self.warned:
                print(f"[WARNING | {get_date()}] [MIKOCORD] Debug is disabled, but log file is enabled. Please disable log file or enable debug.")
                self.warned = True
