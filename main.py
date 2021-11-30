import logging
from aiogram import Bot, Dispatcher, executor, types,filters
from keyboards import replyMarkups as rpk
from keyboards import inlineMarkups as inl
from DataBase import db as DB
from Logic import BotLogic as BL
from Logic import InlineLogic as IL
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled

API_TOKEN = '*TOKEN*'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
@dp.throttled(rate=1)
async def send_welcome(message: types.Message):
    await message.reply("Привет👋. Я Habrot. Я помогу тебе быть в курсе последних " +
                        "статей на habr.com, тех разделов, которые тебе интересны. \n\n Внизу есть клавиатура, благодаря которой ты "+
                        " можешь взаимодейстовать со мной. \n\n Если есть вопросы пиши /help, я всегда рад помочь"
                        ,reply_markup=rpk.MainMenu)
    DB.add_user(message.from_user.id)

@dp.message_handler(commands=['help'])
@dp.throttled(rate=1)
async def help_message(message: types.Message):
    await message.reply("✨Доcтупные команды✨\n\n"
             +  "Начать\\закончить работу с ботом\n"
            + "/start - начать работу со мной\n"
            + "/stop - приостановить работу со мной \n"
            + "/help - получить помощь в работе со мной\n"
            + "\n\n"
            + "Внизу ты можешь заметить кнопки. Через них можешь работать со мной. \n\n"
            + "Кнопка 'Мои Подписки 📰' - посмотреть твои активные подписки\n\n"
            + "Кнопки 'Подписаться на группу ➕' и 'Отписаться от группы ➖'- позволяют взаимодействовать с подписками\n\n"
            + "Так же если ты хочешь сообщить об ошибках багах или хочешь связаться с моими разработчиками вот электронная почта: bbb333bbbzvv@gmail.com")

@dp.message_handler(commands=['stop'])
@dp.throttled(rate=1)
async def btnStopCommand(message: types.message):
    await Stop(message)

@dp.message_handler(filters.Text(equals="Мои Подписки 📰"))
@dp.throttled(rate=1)
async def MySubs(message: types.Message):
    await BL.myGroups(message)

@dp.message_handler(filters.Text(equals="Подписаться на группу ➕"))
@dp.throttled(rate=1)
async def addGroup(message: types.Message):
    await BL.addGroup(message)

@dp.message_handler(filters.Text(equals="Отписаться от группы ➖"))
@dp.throttled(rate=1)
async def DeleteGroup(message: types.Message):
    await BL.deleteGroup(message)

@dp.message_handler(filters.Text(equals="Остановить работу 🛑"))
@dp.throttled(rate=1)
async def Stop(message: types.Message):
    await BL.deactivateUser(message)

@dp.message_handler(filters.Text(equals="Помощь ❓"))
@dp.throttled(rate=1)
async def HelpBtn(message: types.Message):
    await help_message(message)

@dp.message_handler()
@dp.throttled(rate=1)
async def echo(message:types.Message):
    found = DB.findSmallHub(message.text)
    if len(found) == 0:
        await bot.send_message(message.from_user.id,"Прости, я ничего не нашел. Попробуй ещё раз ввести название хаба")
    else:
        x = 1
        kb = types.InlineKeyboardMarkup(row_width=4)
        msg = " 🔎 Вот что я нашел:\n\n"
        for i in found:
            msg += str(x) + ": " + i[1] + "\n"
            kb.insert(types.InlineKeyboardButton(text=x, callback_data=x))
            x += 1
            if x == 11:
                break
        msg += "\nНиже можешь выбрать куда хочешь подписаться"
        await bot.send_message(message.from_user.id, msg, reply_markup=kb)

#---------------------------------- CallBack Handler --------------------------------------------
@dp.callback_query_handler(text="smallHub")
async def btnSmallHub(message: types.Message):
    await bot.edit_message_text(message.message.text, message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id,"Хорошо теперь просто напиши мне название хаба, на который ты хочешь подписаться.\nА я его поищу для тебя")


@dp.callback_query_handler(text="No")
async def btnNo(message: types.Message):
    await bot.edit_message_text(message.message.text, message.from_user.id, message.message.message_id)
    await bot.send_message(message.from_user.id, "Хорошо, теперь как только появится новая статтья, я тебе уведомлю")

@dp.callback_query_handler(text="Yes")
async def btnYes(message: types.Message):
    await bot.edit_message_text(message.message.text, message.from_user.id, message.message.message_id)
    listText = (message.message.text.split())  # Разбить весь текст в массив
    Text = ""
    for i in range(message.message.text.split().index("хаб:") + 1, message.message.text.split().index("Хотите")):
            Text += listText[i] + " "
    Text = Text.rstrip()
    await BL.getLast(message, Text)



@dp.callback_query_handler(lambda call: True)
async def callback_inline(call):
    await bot.edit_message_text(call.message.text, call.from_user.id, call.message.message_id)
    await IL.requestOnUnknownInline(call)


#----------------------------------- Scheduled ------------------------------------
async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        await BL.Schedule()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(900))
    executor.start_polling(dp, skip_updates=True)