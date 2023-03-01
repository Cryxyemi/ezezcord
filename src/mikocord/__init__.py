__title__ = "mikocord"
__author__ = "Cryxyemi"
__license__ = "MIT"
__version__ = "1.8.5"

from .bot import Bot
from .utils.ver_check import version

version._check(__version__)
