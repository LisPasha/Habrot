import sqlite3
__connection = None

def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('DataBase/db.db') # Путь указывается относительно скрипта main.py
    return __connection

#Функция, которая добавит нового пользователя если такого нет в базе.
def add_user(user_id_t:int):
    conn = get_connection()
    c = conn.cursor()
    doesExist = c.execute("SELECT * FROM users WHERE chat_id = ? ", (user_id_t,)).fetchall()
    if (len(doesExist)) == 0:
        c.execute("INSERT OR IGNORE INTO users (chat_id,activity) VALUES (?,?) ", (user_id_t,1,))
        conn.commit()
    else:
        c.execute("UPDATE users SET activity = 1 WHERE chat_id = ?", (user_id_t,))
        conn.commit()


#Функция которая делает пользователя неактивным
def deactivateUser(user_id:int):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE users SET activity = 0 WHERE chat_id = ?", (user_id,))
    conn.commit()

def findSmallHub(text:str):
    conn = get_connection()
    c = conn.cursor()
    found = c.execute("SELECT * FROM subscriptions WHERE name LIKE ? ", ('%'+text+'%',)).fetchall()
    return found

def doesIsUserActivity(user_id:int):
    conn = get_connection()
    c = conn.cursor()
    doesIsActiv = c.execute("SELECT activity FROM users WHERE chat_id = ? ",(user_id,)).fetchall()
    if doesIsActiv == 1:
        return True
    else:
        return False

#------------------------ Работы с таблицой групп ----------------------------------

#Получить список групп на которые можно подписаться
def listOfGroups():
    conn = get_connection()
    c = conn.cursor()
    groupList = c.execute("SELECT * FROM subscriptions").fetchall()
    return groupList

#Получить id группы по её имени
def getIdHubByName(name:str):
    conn = get_connection()
    c = conn.cursor()
    id = c.execute("SELECT * FROM subscriptions WHERE name = ?", (name,)).fetchall()
    return id[0][0]

#Получает имя по id группы:
def getNameHubById(id_sub:int):
    conn = get_connection()
    c = conn.cursor()
    name = c.execute("SELECT name FROM subscriptions WHERE id= ?", (id_sub,)).fetchall()
    return name

#Проверяет подписан ли пользователя на группу по ид группы
def isUserSubOnGroup(user_id:int, id_sub:int):
    conn = get_connection()
    c = conn.cursor()
    doesExist = c.execute("SELECT * FROM users_subscriptions WHERE user_id = ? and subs_id = ?",
                          (user_id, id_sub,)).fetchall()
    if (len(doesExist)) == 0:
        return True
    else:
        return False

#Подписать человека на группу
def subUserToGroup(user_id:int, id_sub:int):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO users_subscriptions (user_id,subs_id) VALUES(?,?) ", (user_id, id_sub,))
    conn.commit()

#Получить список групп на которые подписан пользователь
def getUserGroups(user_id:int):
    conn = get_connection()
    c = conn.cursor()
    userGroups = c.execute("SELECT * FROM users_subscriptions WHERE user_id = ? ", (user_id,)).fetchall()
    userList = []
    for i in userGroups:
        userList.append(getNameHubById(i[2]))

    return userList

#Отписать человека от группы
def unsubUserFromGroup(user_id:int, id_sub:int):
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM users_subscriptions WHERE user_id = ? AND subs_id = ? ", (user_id, id_sub,))
    conn.commit()

#--------------------------------- Функции для автоматической рассылки статтей ----------------------------

#Узнать на какие подсайты вообще подписан хотябы один пользователь:
def activityHubs():
    conn = get_connection()
    c = conn.cursor()
    lists = c.execute("SELECT subs_id FROM users_subscriptions GROUP BY subs_id").fetchall()
    return lists

#Получить RSS ссылку хаба
def getRSSLinkOfHub(id_hub:int):
    conn = get_connection()
    c = conn.cursor()
    rss = c.execute("SELECT rss_link FROM subscriptions WHERE id = ?", (id_hub,)).fetchall()
    return rss[0][0]

#Получить последюю статью хаба
def getLastArticle(id_hub:int):
    conn = get_connection()
    c = conn.cursor()
    art = c.execute("SELECT last_art_id FROM subscriptions WHERE id = ?", (id_hub,)).fetchall()
    return art[0][0]

#Смотрим кому нужно отправлять
def userToSend(id_hub:int):
    conn = get_connection()
    c = conn.cursor()
    userList = c.execute("SELECT user_id FROM users_subscriptions WHERE subs_id = ?", (id_hub,)).fetchall()
    return userList


#Обнволяем последнюю статью
def updateCurrentLink(id_hub:int,link:str):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE subscriptions SET last_art_id = ? WHERE id = ?", (link, id_hub,))
    conn.commit()

