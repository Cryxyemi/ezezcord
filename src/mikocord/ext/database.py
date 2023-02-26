import asyncio
from typing import Coroutine
from enum import Enum

import aiosqlite


class Database:
    class FetchTypes(Enum):
        ONE = 1
        ALL = 2
        MANY = 3

    @classmethod
    def execute(cls, func: Coroutine):
        if not asyncio.iscoroutinefunction(func):
            raise TypeError(f"{func.__repr__()}  must be a coroutine")
            
        async def wrapper(*args, **kw):
            code = await func(*args, **kw)
            
            async with aiosqlite.connect('test.db') as db:
                await db.execute(code, args)
                
                await db.commit()
                
            return "This should work"
            
        return wrapper

    @classmethod
    def fetch(cls, fetch: FetchTypes = FetchTypes.ONE):
        def inner(func: Coroutine):
            if not asyncio.iscoroutinefunction(func):
                raise TypeError(f"{func.__repr__()} must be a coroutine")
            
            async def wrapper(*args, **kw):
                code = await func(*args, **kw)
                
                async with aiosqlite.connect('test.db') as db:
                    async with db.execute(code, args) as cursor:
                        if fetch == cls.FetchTypes.ONE:
                            return await cursor.fetchone()
                        
                        elif fetch == cls.FetchTypes.ALL:
                            return await cursor.fetchall()
                        
                        elif fetch == cls.FetchTypes.MANY:
                            return await cursor.fetchmany()
                        
                        else:
                            raise ValueError(f"Invalid fetch type, expected Fetch.ONE, Fetch.ALL or Fetch.MANY, got {fetch}")
                
            return wrapper
        
        return inner
