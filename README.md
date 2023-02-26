# EzCord

An easy-to-use extension for the [Pycord](https://github.com/Pycord-Development/pycord) library with some utility functions.

## Installing

Python 3.8 or higher is required.

``` cmd
pip install ezcord
```

You can also install the latest version from GitHub. Note that this version may be unstable
and requires [git](https://git-scm.com/downloads) to be installed.

``` cmd
pip install git+https://github.com/tibue99/ezcord
```

## Useful Links

- [Documentation](https://ezcord.readthedocs.io/)
- [Getting started](https://ezcord.readthedocs.io/en/latest/pages/getting_started.html)
- [PyPi](https://pypi.org/project/ezcord/)
- [Pycord Docs](https://docs.pycord.dev/)

## Example

```py
import ezcord
import discord

bot = ezcord.Bot(
    intents=discord.Intents.default()
)

if __name__ == "__main__":
    bot.load_cogs("cogs")  # Load all cogs in the "cogs" folder
    bot.run("TOKEN")
```

**Note:** It's recommended to load the token from a [`.env`](https://pypi.org/project/python-dotenv/) file, from a [`json file`](https://docs.python.org/3/library/json.html) or a normal [`python file`](https://docs.python.org/3/tutorial/modules.html)
instead of hardcoding it.

## Contributing

I am always happy to receive contributions. Here is how to do it:

1. Fork this repository
2. Make changes
3. Create a pull request

You can also [create an issue](https://github.com/tibue99/ezcord/issues/new) if you find any bugs.
