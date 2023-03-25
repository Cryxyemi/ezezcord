from .modules import (
    Embeds,
    ModalIO,
    Colors,
)
from .ext import (
    execute,
    FetchTypes,
    JsonParser,
)
from .utils.log import Log
from .utils.ver_check import version
from .bot import Bot, _version

__title__ = "mikocord"
__author__ = "Cryxyemi"
__license__ = "MIT"
__version__ = _version


version._check(_version)
