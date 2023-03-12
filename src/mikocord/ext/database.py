import asyncio
from typing import Coroutine
from enum import Enum

import aiosqlite


class FetchTypes(Enum):
    """The fetch type for the execute decorator."""
    ONE = 1
    ALL = 2
    NONE = 3

def execute(database: str = "main.db", fetch: FetchTypes = FetchTypes.NONE):
    """Execute a SQL query in a coroutine.

    Arguments
    ---------
    ``database`` (``str``, optional): The database where it should execute the query. Defaults to "main.db".

    ``fetch`` (``FetchTypes``, optional): The fetch type, seen ``FetchTypes``. Defaults to ``FetchTypes.NONE``.
    """
    def inner(func: Coroutine):
        if not asyncio.iscoroutinefunction(func):
            raise TypeError(f"{func.__repr__()}  must be a coroutine")
            
        async def wrapper(*args, **kw):
            code = await func(*args, **kw)

            if fetch == FetchTypes.NONE:
                async with aiosqlite.connect(database) as db:
                    await db.execute(code, args)
                    
                    await db.commit()
                return True
            else:
                async with aiosqlite.connect(database) as db:
                    async with db.execute(code, args) as cursor:
                        if fetch == FetchTypes.ONE:
                            return await cursor.fetchone()
                        elif fetch == FetchTypes.ALL:
                            return await cursor.fetchall()
                        else:
                            raise ValueError(f"Invalid fetch type, expected 'Fetch.ONE' or 'Fetch.ALL', got '{fetch}'")
        return wrapper
    return inner
