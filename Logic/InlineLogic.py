from Logic import BotLogic as BL


async def requestOnUnknownInline(call):
    listText = (call.message.text.split())  # Разбить весь текст в массив
    Text = ""
    if call.data == '1':
        try:
            for i in range(call.message.text.split().index("1:") + 1, call.message.text.split().index("2:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("1:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "

    elif call.data == '2':
        try:
            for i in range(call.message.text.split().index("2:") + 1, call.message.text.split().index("3:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("2:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "

    elif call.data == '3':
        try:
            for i in range(call.message.text.split().index("3:") + 1, call.message.text.split().index("4:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("3:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "
    elif call.data == '4':
        try:
            for i in range(call.message.text.split().index("4:") + 1, call.message.text.split().index("5:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("4:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "

    elif call.data == '5':
        try:
            for i in range(call.message.text.split().index("5:") + 1, call.message.text.split().index("6:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("5:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "

    elif call.data == '6':
        try:
            for i in range(call.message.text.split().index("6:") + 1, call.message.text.split().index("7:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("6:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "
    elif call.data == '7':
        try:
            for i in range(call.message.text.split().index("7:") + 1, call.message.text.split().index("8:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("7:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "
    elif call.data == '8':
        try:
            for i in range(call.message.text.split().index("8:") + 1, call.message.text.split().index("9:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("8:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "
    elif call.data == '9':
        try:
            for i in range(call.message.text.split().index("9:") + 1, call.message.text.split().index("10:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("9:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "
    elif call.data == '10':
        try:
            for i in range(call.message.text.split().index("10:") + 1, call.message.text.split().index("11:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("10:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "
    elif call.data == '11':
        try:
            for i in range(call.message.text.split().index("11:") + 1, call.message.text.split().index("12:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("11:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "
    elif call.data == '12':
        try:
            for i in range(call.message.text.split().index("12:") + 1, call.message.text.split().index("13:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("12:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "
    elif call.data == '13':
        try:
            for i in range(call.message.text.split().index("13:") + 1, call.message.text.split().index("14:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("13:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "
    elif call.data == '14':
        try:
            for i in range(call.message.text.split().index("14:") + 1, call.message.text.split().index("15:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("14:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "
    elif call.data == '15':
        try:
            for i in range(call.message.text.split().index("15:") + 1, call.message.text.split().index("16:")):
                Text += listText[i] + " "
        except(ValueError):
            for i in range(call.message.text.split().index("15:") + 1, call.message.text.split().index("Ниже")):
                Text += listText[i] + " "

    if call.message.text.find("📃") != - 1:
        await BL.addToGroup(call, Text)
    elif call.message.text.find("🔎") != - 1:
        await BL.addToGroup(call, Text)
    else:
        await BL.deleteFromGroup(call, Text)