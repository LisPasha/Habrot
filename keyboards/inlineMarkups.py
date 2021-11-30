from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#------------------------------ Yes/No ------------------------------------------
btnYesNO = InlineKeyboardMarkup(row_width=2)
btnYes = InlineKeyboardButton(text="Да", callback_data="Yes")
btnNo = InlineKeyboardButton(text="Нет", callback_data="No")

btnYesNO.insert(btnNo)
btnYesNO.insert(btnYes)


# ---------------------- Options of Answer -----------------------------
answerOptions = InlineKeyboardMarkup(row_width=3, one_time_keyboard=True)
btnA = InlineKeyboardButton(text="1", callback_data='1')
btnB = InlineKeyboardButton(text="2", callback_data='2')
btnC = InlineKeyboardButton(text="3", callback_data='3')
btnD = InlineKeyboardButton(text="4", callback_data='4')
btnE = InlineKeyboardButton(text="5", callback_data='5')
btnF = InlineKeyboardButton(text="6", callback_data='6')

answerOptions.insert(btnA)
answerOptions.insert(btnB)
answerOptions.insert(btnC)
answerOptions.insert(btnD)
answerOptions.insert(btnE)
answerOptions.insert(btnF)
