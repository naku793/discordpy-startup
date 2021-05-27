from discord.ext import commands
import os
import traceback
import random
import asyncio #sleepを使うのに必要

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
if message.content == "slot":
kakuritu = random.randint(1, 399)
slot_list = ['\U00002660', '\U00002663', '\U00002665', '\U00002666', ':seven:']
A = random.choice(slot_list)
B = random.choice(slot_list)
C = random.choice(slot_list)
if int(kakuritu) == int(1): #確率は1 /399
await client.send_message(message.channel, "ボーナス確定！！！")
await asyncio.sleep(3) #3秒間待ってやる
await client.send_message(message.channel, ':seven:', ':seven:', ':seven:') #7だけ出るように指定
else:
await client.send_message(message.channel, "%s%s%s" % (A, B, C))


bot.run(token)
