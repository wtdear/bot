import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="de", help_command=None, intents=disnake.Intents.all())
    
    
@bot.event
async def on_ready():
    print(f"Bot {bot.user} gotov pahat' na was nachal'nik!")

@bot.event
async def on_member_join(Member):
    guild_id=Member.guild.id
    guild = bot.get_guild(guild_id)
    role = guild.get_role(1068184941650784336)
    channel = bot.get_channel(998624808675848194)

    embed = disnake.Embed(
        title="Добро пожаловать!",
        description=f"{Member.name}",
        color=0x9932cc
    )

    await Member.add_roles(role)
    await channel.send(embed=embed)

@bot.slash_command()
async def hello(ctx):
    await ctx.send(f"{ctx.author.mention}, Васап!")

@bot.slash_command()
async def myname(ctx):
    await ctx.send(f"{ctx.author.name}, nice")

bot.run("MTA2NzQ3ODgxODQwNDcwNDI5Nw.GyYiTR.DXT2D_xBpBr7WpvZp_kV_lEEq4p84Vi5686f9w")