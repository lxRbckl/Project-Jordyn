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
token = 'OTUwNjk0MTQ3MTU5OTA0Mjc2.Yico6w.fC6iKI_oFtWxfU9z9Y9Pc6pubGo'
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


@jordyn.command(aliases = jsonLoad(file = '/setting.json')['aliases']['choose'])
async def chooseCommand(ctx, *args):
    '''  '''

    # decide choice <
    # output choice <
    decision = choice(' '.join(args).split(',')).strip()
    await ctx.send(f':arrow_forward: **{decision}**', delete_after = 540)
    xx = 'lxRbckl#2812'
    await ctx.xx.send('test', delete_after = 4)

    # >


@jordyn.command(aliases = jsonLoad(file = '/setting.json')['aliases']['conch'])
async def conchCommand(ctx, arg):
    '''  '''

    # decide choice <
    # output choice <
    decision = choice(jsonLoad(file = '/setting.json')['conch'])
    await ctx.send(f'**{decision}**', delete_after = 540)

    # >


@jordyn.command(aliases = jsonLoad(file = '/setting.json')['aliases']['address'])
async def addressCommand(ctx, address: str = None):
    '''  '''

    # local <
    data = jsonLoad(file = '/data.json')

    # >

    # if (new user) then add user <
    if (str(ctx.author)[:-5] not in data.keys()):

        # default user structure <
        # add user to data <
        # set data <
        structure = {'userId' : ctx.author.id, 'address' : {}, 'mail' : {}}
        data[str(ctx.author)[:-5]] = structure
        jsonDump(file = '/data.json', data = data)

        # >

        # generate added message <
        # notify user <
        added = (f'Welcome, **{str(ctx.author)[:-5]}**!')
        await ctx.author.send(added)

        # >

    # >

    # if (no address) then get address <
    if (address is None):

        # get author from data <
        # get address(es) from author <
        address = data[str(ctx.author)[:-5]]['address']
        output = '\n'.join(f'{c + 1}.\t*{a}*' for c, a in enumerate(address))

        # >

        # output address(es) <
        await ctx.author.send(output, delete_after = 60)

        # >

    # >

    # else then add address <
    else:

        # iterate (author) in data <
        for userId, userData in data.items():

            # if (address exists) then exit <
            if (address in userData['address']):

                # generate error message <
                # notify user <
                # exit <
                error = (f'Address **{address}** already exists.')
                await ctx.author.send(error, delete_after = 60)
                break

                # >

            # >

        # >

        # else (new address) <
        else:

            # add address <
            # set data <
            data[str(ctx.author)[:-5]]['address'].append(address)
            jsonDump(file = '/data.json', data = data)

            # >

            # generate success message <
            # notify user <
            success = (f'Address **{address}** was created.')
            await ctx.author.send(success, delete_after = 60)

            # >

        # >

    # >


@jordyn.command(aliases = jsonLoad(file = '/setting.json')['aliases']['inbox'])
async def inboxCommand(ctx, parAddress: str = None):
    '''  '''

    # local <
    summary = {}
    data = jsonLoad(file = '/data.json')
    mail = data[str(ctx.author)[:-5]]['mail'].values()
    emojiUnread, emojiRead = ':mailbox:', ':mailbox_with_no_mail:'

    # >

    # build summary <
    for address, subject, message, condition in mail:

        # if (new address) then assign structure <
        if (address not in summary.keys()):

            # default count structure <
            # set structure to address <
            structure = {'read' : 0, 'unread' : 0}
            summary[address] = structure

            # >

        # >

        # if (condition True) then read <
        # else then unread <
        if (condition is True): summary[address]['read'] += 1
        elif (condition is False): summary[address]['unread'] += 1

        # >

    # >

    # if (no parameter) then summary <
    if (parAddress is None):

        # declare message <
        # iterate (address, count) in summary <
        allInbox = ''
        for address, count in summary.items():

            # add address <
            # add unread mail <
            # add read mail <
            inbox = '**{}**\t'.format(address)
            inbox += '{} **{}**\t'.format(emojiUnread, count['unread'])
            inbox += '{} **{}**\n'.format(emojiRead, count['read'])

            # >

            # add inbox to message <
            allInbox += inbox

            # >

        # >

        # send message to user <
        await ctx.author.send(allInbox, delete_after = 180)

        # >

    # >

    # elif (address parameter only) then address summary <
    elif (parAddress is not None):

        # build read and unread <
        inboxRead, inboxUnread = [], []
        for mailId, mailData in data[str(ctx.author)[:-5]]['mail'].items():

            # if (address match) then add <
            if (mailData[0] == parAddress):

                # if (read) then add to read list <
                # else unread then add to unread list <
                if (mailData[3] is True): inboxRead.append([mailId, mailData])
                else: inboxUnread.append([mailId, mailData])

                # >

            # >

        # >

        # add unread mail <
        inbox = '\n{} **{} Unread**\n\n'.format(emojiUnread, summary[parAddress]['unread'])
        for mailId, mailData in inboxUnread: inbox += (f'{mailId}.\t{mailData[1]}\n')

        # >

        # add read mail <
        inbox += '\n{} **{} Read**\n\n'.format(emojiRead, summary[parAddress]['read'])
        for mailId, mailData in inboxRead: inbox += (f'{mailId}.\t{mailData[1]}\n')

        # >

        # send message to user <
        await ctx.author.send(inbox, delete_after = 180)

        # >

    # >


@jordyn.command(aliases = jsonLoad(file = '/setting.json')['aliases']['read'])
async def readCommand(ctx, mailId: str):
    '''  '''

    # local <
    data = jsonLoad(file = '/data.json')
    mail = data[str(ctx.author)[:-5]]['mail']

    # >

    # mark read <
    # update data <
    # generate message for user <
    mail[mailId][3] = True
    data[str(ctx.author)[:-5]]['mail'] = mail
    message = (f'Subect: {mail[mailId][1]}\nMessage: {mail[mailId][2]}')

    # >

    # send message to user <
    # set data <
    await ctx.author.send(message, delete_after = 540)
    jsonDump(file = '/data.json', data = data)

    # >


@jordyn.command(aliases = jsonLoad(file = '/setting.json')['aliases']['compose'])
async def composeCommand(ctx, parAddress: str, *args):
    '''  '''

    # local <
    content = ' '.join(args).split('/')
    data = jsonLoad(file = '/data.json')
    emojiWarning, emojiMail = ':warning:', ':envelope:'
    subject, message = content[0], ' '.join(content[1:])

    # >

    # iterate (user) in data <
    for user in data:

        # if (address match) then send <
        if (parAddress in user['address']):

            # get unique mail id <
            # update data <
            mailId = len(data[user]['mail']) + 1
            data[user]['mail'][str(mailId)] = [parAddress, subject.strip(), message.strip(), False]

            # >

            # notify receiver <
            # notify sender <
            receiver = (f'*{str(ctx.author)[:-5]}* send you a message to **{parAddress}**')
            sender = (f'Your message was successfully delivered to **{parAddress}**')
            await jordyn.get_user(user['userId']).send(receiver)
            await ctx.author.send(receiver)

            # >

            # set data <
            # exit loop <
            jsonDump(file = '/data.json', data = data)
            break

            # >

        # >

    # >

    # else then not found <
    else:

        # generate warning message <
        # notify sender <
        warning = f'{emojiWarning} The address **{parAddress}** could not be found!'
        ctx.author.send(warning, delete_after = 180)

        # >

    # >


# main <
if (__name__ == '__main__'):

    jordyn.run(token)

# >
