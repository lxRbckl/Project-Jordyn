# Project Jordyn by Alex Arbuckle #


# import <
from os import path
from random import choice
from json import load, dump
from discord import Intents
from discord.ext import commands

# >


# global <
path = path.realpath(__file__).split('/')
directory = '/'.join(path[:(len(path) - 1)])
token = ''
jordyn = commands.Bot(

    command_prefix = '',
    intents = Intents.all()

)

# >


def jsonLoad(file: str):
    '''  '''

    # get file <
    # get data <
    with open(f'{directory}{file}', 'r') as fin:

        return load(fin)

    # >


def jsonDump(file: str, data: dict):
    '''  '''

    # set file <
    # set data <
    with open(f'{directory}{file}', 'w') as fout:

        dump(data, fout, indent = 3)

    # >


async def chooseFunction(ctx, options: tuple) -> None:
    '''  '''

    # choose input <
    # send output <
    out = choice(' '.join(options).split(',')).strip()
    await ctx.send(f':arrow_forward: **{out}**', delete_after = 540)

    # >


async def addressFunction(ctx, data: dict, address: str) -> dict:
    '''  '''

    # if (new address) <
    if (address not in data['mail'].keys()):

        # update mail <
        # delete message <
        data['mail'][address] = {}
        await ctx.message.delete()

        # >

    # >

    # output <
    return data

    # >


async def inboxFunction(ctx, data: dict, *args) -> dict:
    '''  '''

    pass


async def composeFunction(ctx, data: dict, *args) -> dict:
    '''  '''

    pass


@jordyn.command(aliases = jsonLoad(file = '/Jordyn.json')['aliases'])
async def commandFunction(ctx, *args):
    '''  '''

    # load <
    data = jsonLoad(file = '/Jordyn.json')

    # >

    # if (choose) <
    # elif (address, inbox or compose) <
    if (ctx.invoked_with.lower() == 'choose'): await chooseFunction(ctx, args)
    elif (ctx.invoked_with.lower() == 'address'): data = await addressFunction(ctx, data, args[0])
    elif (ctx.invoked_with.lower() == 'inbox'): pass
    elif (ctx.invoked_with.lower() == 'compose'): pass

    # >

    # dump <
    jsonDump(file = '/Jordyn.json', data = data)

    # >


# main <
if (__name__ == '__main__'):

    jordyn.run(token)

# >
