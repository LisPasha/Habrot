from aiogram import Bot, Dispatcher, executor, types,filters
from main import bot
from keyboards import replyMarkups as rpk
from keyboards import inlineMarkups as inl
from DataBase import db as DB
from Parser import RSS_Parser as RP


#Показывает список доступных групп, и вызывает клавиатуру под неё
async def addGroup(message:types.Message):
    x = 1 # Счетчик, чтобы выводить кнопки, и структурировать сообщение
    kb = types.InlineKeyboardMarkup(row_width=3) # Создание новой клавиатуры
    group_list = DB.listOfGroups() # Получаем список групп
    msg = " 📃 Список доступных групп:\n\n"
    for i in group_list: # Выводим имя каждой группы в форму 1: Имя группы и сразу создаем под неё кнопку
        msg += str(x) + ": " + i[1] + "\n"
        kb.insert(types.InlineKeyboardButton(text=x, callback_data=x))
        x += 1
        if x == 7:
            break
    kb.insert(types.InlineKeyboardButton(text="Хочу узкоспециализрованный хаб", callback_data="smallHub"))
    msg += "\nНиже можешь выбрать куда хочешь подписаться"
    await bot.send_message(message.from_user.id, msg, reply_markup=kb)


# Обращаться к базе чтобы подписать человека
async def addToGroup(message: types.Message, text:str):
    #text = text.replace(' ', '')
    text = text.rstrip()
    idSub = DB.getIdHubByName(text)
    if DB.isUserSubOnGroup(message.from_user.id,idSub) == True:
        DB.subUserToGroup(message.from_user.id,idSub)
        await bot.send_message(message.from_user.id,"Подписал вас на хаб: " + text +
                               "\nХотите получить последнюю статью с этого хаба?", reply_markup=inl.btnYesNO)
    else:
        await bot.send_message(message.from_user.id,"Вы уже подписаны на хаб '" + text + '"')

async def deactivateUser(message: types.Message):
    DB.deactivateUser(message.from_user.id)
    await bot.send_message(message.from_user.id,"Деактивировал вашу активность 😟. \n\nТеперь уведомления не будут приходить." +
                           " Но если захочешь вернуться напиши снова /start. И не переживай все твой подписки в сохраности!")

#Выводит все подписки пользователя
async def myGroups(message:types.Message):
    x = 1  # Счетчик, чтобы структурировать сообщение
    group_list = DB.getUserGroups(message.from_user.id) # Получаем список групп
    msg = "📖 Ваши подписки: 📖\n\n"
    if len(group_list) != 0:
        for i in group_list:
            msg += str(x) + ": " + i[0][0] + "\n"
            x += 1
        await bot.send_message(message.from_user.id, msg)
    else:
        await bot.send_message(message.from_user.id, "Ты ещё не подписан не на один хаб.\nЧтобы подписаться используй кнопку 'Подписаться на группу ➕'")

async def deleteGroup(message:types.Message):
    group_list = DB.getUserGroups(message.from_user.id)
    kb = types.InlineKeyboardMarkup(row_width=4)
    x = 1
    if len(group_list) != 0:
        msg = "❓ От чего хотите отписаться? ❓\n\n"
        for i in group_list:
            msg += str(x) + ": " + i[0][0] + "\n"
            kb.insert(types.InlineKeyboardButton(text=x, callback_data=x))
            x += 1

        msg += "\n Ниже выбор"
        await bot.send_message(message.from_user.id, msg, reply_markup=kb)
    else:
        await bot.send_message(message.from_user.id, "Вы не подписаны не на один хаб")

async def deleteFromGroup(message:types.Message, text:str):
    text = text.rstrip()
    id_hub = DB.getIdHubByName(text)
    DB.unsubUserFromGroup(message.from_user.id,id_hub)
    await bot.send_message(message.from_user.id, "Отписал вас от хаба '" + text + '"')

#---------------------------- Schedule Logic ----------------------------------------
async def Schedule():
    activityHub = DB.activityHubs()
    if len(activityHub) != 0:
        for i in activityHub:
            rss_link = DB.getRSSLinkOfHub(i[0]) # Получаем RSS ссылку на группу
            last_art = DB.getLastArticle(i[0]) # Получаем ссылку последней статьи
            currentLink = RP.getLastArticleAll(rss_link) # Получаем последнюю статью на подсайте

            if currentLink == last_art: # Сравниваем послендюю статью и текущую
                print("Новых нет")
                continue
            else:
                print("Новые есть")
                users = DB.userToSend(i[0]) # Узнаем каким пользователям нужно отправить статью
                name = DB.getNameHubById(i[0]) # Получаем имя группы чтобы уведомить пользователя
                for m in users:
                    # В тестов режиме проверка активности
                    await bot.send_message(m[0], "Новая статья с хаба: " + name[0][0])
                    await bot.send_message(m[0], currentLink)
                DB.updateCurrentLink(i[0], currentLink) # Обновляем статью
    else:
        pass

#----------------------------------- Get Last Aricle ------------------------------
async def getLast(message:types.message, text:str):
    idSub = DB.getIdHubByName(text)
    rss_link = DB.getRSSLinkOfHub(idSub)
    last_art = DB.getLastArticle(idSub)
    currentLink = RP.getLastArticleAll(rss_link)
    if currentLink == last_art:
        await bot.send_message(message.from_user.id,currentLink)
    else:
        DB.updateCurrentLink(idSub, currentLink)
        await bot.send_message(message.from_user.id, currentLink)




