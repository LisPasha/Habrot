from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btnMyGroups = KeyboardButton("Мои Подписки 📰")
btnAddGroup = KeyboardButton("Подписаться на группу ➕")
btnDelGroup = KeyboardButton("Отписаться от группы ➖")
btnHelp = KeyboardButton("Помощь ❓")
btnStop = KeyboardButton("Остановить работу 🛑")


MainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnMyGroups,btnAddGroup,btnDelGroup,btnStop,btnHelp)
