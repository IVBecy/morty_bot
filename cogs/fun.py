"""

A cog for all the fun functions

"""
# Libs
from helpers.loader import *
# Additional libs
import helpers.nsfw as nsfw,helpers.memes as memes

class Fun(commands.Cog):
  def __init__(self,bot):
    self.bot = bot


  # Pepe meter
  @commands.command(name="pee-pee",aliases=["PEE-PEE"])
  async def pepe(self,ctx):
      size = random.randrange(1,25)
      await ctx.send(embed=make_embed(f"{ctx.message.author.name}'s size",f"8{'='*size}D",discord.Color.from_rgb(*EMBED_COLORS["greenyellow"])))
      logger.Log("PEE-PEE",ctx.guild,ctx.message.author.name,time.ctime()).action()

  # NSFW
  @commands.command(name="nsfw",aliases=["NSFW"])
  async def nsfw(self,ctx):
      link = random.choice(nsfw.FUNCTIONS)()
      embed = discord.Embed(
      color=discord.Color.from_rgb(*EMBED_COLORS["magenta"]))
      embed.set_image(url=link)
      await ctx.send(embed=embed) 
      logger.Log("NSFW",ctx.guild,ctx.message.author.name,time.ctime()).action()

 # MEMES
  @commands.command(name="meme",aliases=["MEME"])
  async def meme(self,ctx):
      link = memes.get_meme()
      embed = discord.Embed(
      color=discord.Color.from_rgb(*EMBED_COLORS["greenyellow"]))
      embed.set_image(url=link)
      await ctx.send(embed=embed) 
      logger.Log("MEME",ctx.guild,ctx.message.author.name,time.ctime()).action()

async def setup(bot):
    await bot.add_cog(Fun(bot))