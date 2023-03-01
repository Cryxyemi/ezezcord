import aiohttp
import asyncio
import threading

from .log import Log


class version:
    @classmethod
    async def _get_version(cls, current_version: str) -> bool:
        log = Log(debug=False, with_date=False)

        async with aiohttp.ClientSession() as session:
            async with session.get("https://raw.githubusercontent.com/Cryxyemi/mikocord/main/src/mikocord/__init__.py") as resp:
                text = await resp.text()
                github_version = text.split("__version__ = ")[1].split("\n")[0].replace('"', "")

        if float(current_version) >= float(github_version):
            return log._force_logger("You are using the latest version of mikocord.", "version", "info")
        else:
            return log._force_logger("You are using an outdated version of mikocord. Please update to the latest version.", "version", "warning")

    @classmethod
    def __check_version(cls, current_version: str) -> None:
        asyncio.run(cls._get_version(current_version))

    @classmethod
    def _check(cls, current_version: str) -> None:
        thread = threading.Thread(target=cls.__check_version, args=(current_version,))

        thread.start()
        thread.join()
