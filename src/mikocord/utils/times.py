from datetime import timezone, datetime, timedelta
from typing import Literal

from discord.utils import format_dt, utcnow


def set_utc(dt: datetime) -> datetime:
    """Set the timezone of a datetime object to UTC.

    Parameters
    ----------
    dt:
        The datetime object to set the timezone of.

    Returns
    -------
    :class:`datetime.datetime`
    """
    return dt.replace(tzinfo=timezone.utc)


def dc_timestamp(
        seconds: int,
        style: Literal["t", "T", "d", "D", "f", "F", "R"] = "R"
) -> str:
    """Convert seconds to a Discord timestamp.

    Parameters
    ----------
    seconds: :class:`int`
        The amount of seconds to convert.
    style: :class:`str`
        The style of the timestamp. Defaults to ``R``.

    Returns
    -------
    :class:`str`
    """
    dt = utcnow() + timedelta(seconds=seconds)
    return format_dt(dt, style)


class Convertor:
    """Converts human time formats into seconds. Best use for unix time"""

    def __init__(self) -> None:
        self.minute = 60
        self.hour = self.minute * 60
        self.day = self.hour * 24

    def from_minute(self, minutes: int) -> int:
        """Converts minute(s) to seconds"""
        
        return round(self.minute * minutes, 100)

    def from_hour(self, hours: int) -> int:
        """Converts hour(s) to seconds"""
        
        return round(self.hour * hours, 100)

    def from_day(self, days: int) -> int:
        """Converts day(s) to seconds"""
        
        return round(self.day * days, 100)

    def to_minute(self, seconds: int) -> int:
        """Converts seconds to minute(s)"""
        
        return round(seconds / self.minute, 100)
    
    def to_hour(self, seconds: int) -> int:
        """Converts seconds to hour(s)"""
        
        return round(seconds / self.hour, 100)

    def to_day(self, seconds: int) -> int:
        """Converts seconds to day(s)"""
        
        return round(seconds / self.day, 100)


def with_date(text):
    """Returnss the current time in the text\n
    ``[Day-Month-Year Hour:Minute:Second] your text``
    """
    cTime = datetime.now()

    # return f"[{cTime.day}-{cTime.month}-{cTime.year} {cTime.hour}:{cTime.minute}:{cTime.second}] {text}"
    return cTime.strftime("%d-%m-%Y %H:%M:%S")


def get_date() -> str:
    """Returns the current time in the format ``Day-Month-Year Hour:Minute:Second``"""
    cTime = datetime.now()

    # return f"{cTime.day}-{cTime.month}-{cTime.year} {cTime.hour}:{cTime.minute}:{cTime.second}"
    return cTime.strftime("%d-%m-%Y %H:%M:%S")