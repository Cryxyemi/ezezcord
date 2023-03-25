__title__ = "mikocord"
__author__ = "Cryxyemi"
__license__ = "MIT"
__version__ = _version

from .bot import Bot, _version

from .utils.ver_check import version
from .utils.log import Log

from .ext import (
    execute,
    FetchTypes,
    JsonParser,
)
from .modules import (
    Embeds,
    ModalIO,
    Colors,
)

version._check(_version)
