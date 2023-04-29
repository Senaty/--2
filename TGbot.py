import aiogram as aio
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random as rnd
from modules.RPS import RSP

rock = RSP.GameItem('Камень', 0, 2, 1)
paper = RSP.GameItem('Бумага', 1, 0, 2)
scissors = RSP.GameItem('Ножницы', 2, 1, 0)

handGame = RSP.handItem(rock, scissors, paper)
EchoText = ['Майкл Джексон гоаорит', 'Руди сладко шепчит', 'Диктор канала мастерская настроения озвучивает']
EchoText2 = ['А ты не делай так', 'А ты стреляй давай, чего медлишь', 'А ты мог бы быть такимже']
Otvets = ['Сори, Ну сорррии, введи команду /help', 'Не пониаю, введи /help', 'Х**ю несёшь, введи /help']

with open('pivacy/DadOrange_bot.txt', 'r') as tokenBot_file:
    thisBotToken = tokenBot_file.read()

thisBot = aio.Bot(thisBotToken)
dp = aio.Dispatcher(thisBot)
flagEcho = 'False'
flagRSP = 'False'

with open('cache/flag_RSP.txt', 'w') as flagRSP_file:
    flagRSP_file.write('False')

with open('cache/flag_echo.txt', 'w') as flagEcho_file:
    flagEcho_file.write(str(flagEcho))

with open('cache/flag_echo.txt', 'r') as flagEcho_file:
    flagEcho = flagEcho_file.read()

with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
    flagRSP = flagRSP_file.read()

BTN_ROCK = InlineKeyboardButton('Камень', callback_data='Rock')
BTN_Scissors = InlineKeyboardButton('Ножницы', callback_data='Scissors')
BTN_RSP_STOP = InlineKeyboardButton('/RSPstop', callback_data='RSPstop')
BTN_PAPER = InlineKeyboardButton('Бумага', callback_data='Paper')

RSP_KB = InlineKeyboardMarkup().add(BTN_ROCK, BTN_Scissors, BTN_PAPER, BTN_RSP_STOP)


@dp.message_handler(commands=["start"])
async def process_start_command(message: aio.types.Message):
    await message.reply("Привет! \nЯ на связи готов к работе! \nНапиши /help и я расскажу что могу")


@dp.message_handler(commands=["help"])
async def process_help_command(message: aio.types.Message):
    await message.reply("/help - список команд \n/echo - эхо-бот \n/RSP - Игра")


@dp.message_handler(commands=["echo"])
async def echo_bot(message: aio.types.Message):
    await message.reply(' Играем в эхо! \nНапиши /echostop, если хочешь закончить')
    flagEcho = "True"
    with open('cache/flag_echo.txt', 'w') as flagEcho_file:
        flagEcho_file.write(str(flagEcho))


@dp.message_handler(commands=["RSP"])
async def RSP_bot(message: aio.types.Message):
    await message.reply(' Играем в КНБ! \nНапиши /RSPstop, если хочешь закончить', reply_markup=RSP_KB)
    flagRSP = "True"
    with open('cache/flag_RSP.txt', 'w') as flagRSP_file:
        flagRSP_file.write(str(flagRSP))


with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
    flagRSP = flagRSP_file.read()


@dp.message_handler(commands=['Rock'])
async def thisRock(message: aio.types.Message):
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'True':
        player_hand = handGame.choise(thisPlayer=True, thisChoise=1)
        bot_hand = handGame.choise(thisPlayer=False, thisChoise=1)
        await thisBot.send_message(message.from_user.id, text=f"{player_hand['msg']}")
        await thisBot.send_message(message.from_user.id, text=f"{bot_hand['msg']}")
        await thisBot.send_message(message.from_user.id,
                                   text=f"{RSP.compareHand(player_hand['Game_Item'], bot_hand['Game_Item'])}")
        await message.reply(f'\n/Rock \n/Scissors \n/Paper')
        await thisBot.send_message(message.from_user.id, text=f"{player_hand['msg']},\n{bot_hand['msg']}",
                                   reply_markup=RSP_KB)


@dp.message_handler(commands=['Scissors'])
async def thisScissors(message: aio.types.Message):
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'True':
        player_hand = handGame.choise(thisPlayer=True, thisChoise=3)
        await thisBot.send_message(message.from_user.id, text=f"{player_hand['msg']}")
        bot_hand = handGame.choise(thisPlayer=False, thisChoise=3)
        await thisBot.send_message(message.from_user.id, text=f"{bot_hand['msg']}")
        await thisBot.send_message(message.from_user.id,
                                   text=f"{RSP.compareHand(player_hand['Game_Item'], bot_hand['Game_Item'])}")
        await message.reply(f'\n/Rock \n/Scissors \n/Paper')
        await thisBot.send_message(message.from_user.id, text=f"{player_hand['msg']},\n{bot_hand['msg']}",
                                   reply_markup=RSP_KB)


@dp.message_handler(commands=['Paper'])
async def thisPaper(message: aio.types.Message):
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'True':
        player_hand = handGame.choise(thisPlayer=True, thisChoise=2)
        await thisBot.send_message(message.from_user.id, text=f"{player_hand['msg']}")
        bot_hand = handGame.choise(thisPlayer=False, thisChoise=2)
        await thisBot.send_message(message.from_user.id, text=f"{bot_hand['msg']}")
        await thisBot.send_message(message.from_user.id,
                                   text=f"{RSP.compareHand(player_hand['Game_Item'], bot_hand['Game_Item'])}")
        await message.reply(f'\n/Rock \n/Scissors \n/Paper')
        await thisBot.send_message(message.from_user.id, text=f"{player_hand['msg']},\n{bot_hand['msg']}",
                                   reply_markup=RSP_KB)


@dp.callback_query_handler(text='Rock')
async def process_callback_rock(callback_query: aio.types.CallbackQuery):
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'True':
        player_hand = handGame.choise(True, 1)
        bot_hand = handGame.choise(False, 1)
        result_msg = RSP.compareHand(player_hand['Game_Item'], bot_hand['Game_Item'])
        await thisBot.answer_callback_query(callback_query.id)
        await thisBot.send_message(callback_query.from_user.id,
                                   text=f"{player_hand['msg']},\n{bot_hand['msg']}, \n{result_msg}",
                                   reply_markup=RSP_KB)
    else:
        await thisBot.send_message(callback_query.from_user.id, rnd.choice(Otvets))


@dp.callback_query_handler(text='Scissors')
async def process_callback_scissors(callback_query: aio.types.CallbackQuery):
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'True':
        player_hand = handGame.choise(True, 3)
        bot_hand = handGame.choise(False, 3)
        result_msg = RSP.compareHand(player_hand['Game_Item'], bot_hand['Game_Item'])
        await thisBot.answer_callback_query(callback_query.id)
        await thisBot.send_message(callback_query.from_user.id,
                                   text=f"{player_hand['msg']},\n{bot_hand['msg']}, \n{result_msg}",
                                   reply_markup=RSP_KB)
    else:
        await thisBot.send_message(callback_query.from_user.id, rnd.choice(Otvets))


@dp.callback_query_handler(text='Paper')
async def process_callback_paper(callback_query: aio.types.CallbackQuery):
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'True':
        player_hand = handGame.choise(True, 2)
        bot_hand = handGame.choise(False, 2)
        result_msg = RSP.compareHand(player_hand['Game_Item'], bot_hand['Game_Item'])
        await thisBot.answer_callback_query(callback_query.id)
        await thisBot.send_message(callback_query.from_user.id,
                                   text=f"{player_hand['msg']},\n{bot_hand['msg']}, \n{result_msg}",
                                   reply_markup=RSP_KB)
    else:
        await thisBot.send_message(callback_query.from_user.id, rnd.choice(Otvets))


@dp.callback_query_handler(text='RSPstop')
async def process_callback_RSPstop(callback_query: aio.types.CallbackQuery):
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
        if flagRSP == 'True':
            await thisBot.answer_callback_query(callback_query.id)
            await thisBot.send_message(callback_query.from_user.id, 'Не играем в КНБ')
            flagRSP = 'False'
            with open('cache/flag_RSP.txt', 'w') as flagRSP_file:
                flagRSP_file.write(str(flagRSP))
        else:
            await thisBot.send_message(callback_query.from_user.id, rnd.choice(Otvets))

@dp.message_handler()
async def get_text_from_message(message: aio.types.Message):
    with open('cache/flag_echo.txt', 'r') as flagEcho_file:
        flagEcho = flagEcho_file.read()
    with open('cache/flag_RSP.txt', 'r') as flagRSP_file:
        flagRSP = flagRSP_file.read()
    if flagRSP == 'False':
        if flagEcho == 'True':
            if message.text != '/echostop':
                await thisBot.send_message(message.from_user.id, f'{rnd.choice(EchoText)} ({message.text})\n {rnd.choice(EchoText2)}')
                flagEcho = 'True'
            elif message.text == '/echostop':
                await thisBot.send_message(message.from_user.id, 'Всё')
                flagEcho = 'False'
        else:
            flagEcho = 'False'
            await message.reply(rnd.choice(Otvets))
        with open('cache/flag_echo.txt', 'w') as flagEcho_file:
            flagEcho_file.write(str(flagEcho))
    else:
        if message.text == '/RSPstop':
            await thisBot.send_message(message.from_user.id, 'Не играем в КНБ')
            flagRSP = 'False'
            with open('cache/flag_RSP.txt', 'w') as flagRSP_file:
                flagRSP_file.write(str(flagRSP))


aio.executor.start_polling(dp)
