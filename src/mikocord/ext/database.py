import asyncio
from typing import Coroutine
from enum import Enum

import aiosqlite


class Database:
    def __init__(self, path: str) -> None:
        self.path = path

    class FetchTypes(Enum):
        """The fetch type for the execute decorator."""
        ONE = 1
        ALL = 2
        NONE = 3

    def __repr__(self) -> str:
        return f"<Database path={self.path}>"

    async def execute_query(self, query: str, args: tuple = None, fetch: FetchTypes = FetchTypes.NONE):
        """The non-decorator version of the `execute` decorator.

        Arguments
        ---------
        ``query`` (``str``): The query to execute.

        ``args`` (``tuple``, optional): The arguments to pass to the query. Defaults to ``None``.

        ``fetch`` (``FetchTypes``, optional): The fetch type, seen ``FetchTypes``. Defaults to ``FetchTypes.NONE``.
        """
        if fetch == self.FetchTypes.NONE:
            async with aiosqlite.connect(self.path) as db:
                await db.execute(query, args)

                await db.commit()
            return True
        else:
            async with aiosqlite.connect(self.path) as db:
                async with db.execute(query, args) as cursor:
                    if fetch == self.FetchTypes.ONE:
                        return await cursor.fetchone()
                    elif fetch == self.FetchTypes.ALL:
                        return await cursor.fetchall()
                    else:
                        raise ValueError(
                            f"Invalid fetch type: {fetch}")

    def execute(self, fetch: FetchTypes = FetchTypes.NONE):
        """A decorator that executes a query.

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

                if fetch == self.FetchTypes.NONE:
                    async with aiosqlite.connect(self.path) as db:
                        await db.execute(code, args)

                        await db.commit()
                    return True
                else:
                    async with aiosqlite.connect(self.path) as db:
                        async with db.execute(code, args) as cursor:
                            if fetch == self.FetchTypes.ONE:
                                return await cursor.fetchone()
                            elif fetch == self.FetchTypes.ALL:
                                return await cursor.fetchall()
                            else:
                                raise ValueError(
                                    f"Invalid fetch type, expected 'Fetch.ONE' or 'Fetch.ALL', got '{fetch}'")
            return wrapper
        return inner
