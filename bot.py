token = ""
from discord import *
from discord.ext import commands
import textwrap



prefix = "!"
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("Everything is ready !")


@bot.event
async def on_message(message):
    print("Testserver log >>>", message.content)
    await bot.process_commands(message)


@bot.command()
async def L(ctx):
    wrapper = textwrap.TextWrapper(width=40)
    dedented_text = textwrap.dedent(text=ctx.message.content[3:])
    original = wrapper.fill(text=dedented_text)
    t = original.split("\n")
    result=""
    for str in t:
        result = "/lore add " + str + "\n"
        await ctx.send(result)