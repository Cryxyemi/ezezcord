__title__ = "mikocord"
__author__ = "Cryxyemi"
__license__ = "MIT"
__version__ = "1.9.1"

from .bot import Bot

from .utils.ver_check import version

from .ext import (
    execute,
    FetchTypes,
    JsonParser,
)
from .modules import (
    Embeds,
    ModalIO,
    Colors,
    FastSelect,
)

version._check(__version__)
