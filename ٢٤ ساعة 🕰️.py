import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
@commands.has_permissions(administrator=True)
async def زاحف(ctx, server_name: str = "زاحف ✌🏻"):
    # نسخة آمنة: تغيّر اسم السيرفر فقط ولا تحذف رومات/رتب
    try:
        await ctx.guild.edit(name=server_name)
        await ctx.send(f"تم تغيير اسم السيرفر إلى **{server_name}**")
    except discord.Forbidden:
        await ctx.send("ما عندي صلاحية تغيير اسم السيرفر")
    except Exception as e:
        await ctx.send(f"حدث خطأ: {e}")

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("ضع توكن البوت في متغير البيئة TOKEN")

bot.run(TOKEN)
