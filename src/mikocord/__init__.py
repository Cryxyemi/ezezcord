__title__ = "mikocord"
__author__ = "Cryxyemi"
__license__ = "MIT"
__version__ = "1.8"

from .bot import Bot
from .utils.ver_check import _check_version

_check_version(__version__)
