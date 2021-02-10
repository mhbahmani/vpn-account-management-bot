from decouple import config
import botogram
import pymongo
from pymongo import MongoClient
import re


bot = botogram.create(config("API_KEY"))
bot.about = config("about")
bot.owner = config("owner")

client = MongoClient()
db = client.vpnbotdb
users = db.users

@bot.command("start")
def add_user(chat, message, args):
    new_user = {"chat_id": chat.id,
                "username": chat.username,
                "first_name": chat.first_name,
                "last_name": chat.last_name}
    users.insert_one(new_user)
    msg = """
Welcome to booooooooooooooooooo bot

تمام خدمات تابع قوانین جمهوری اسلامی ایران است🇮🇷
 تنها راه نجات = اطاعت از رهبری
 این پیروزیییییییییی، خسجته باد این پیروزیییییییییییییییییییی🥳
    """
    chat.send(msg)


broadcast_command_w_msg = config("broadcast_command_w_msg")
@bot.message_contains(broadcast_command_w_msg)
def broadcast_message(chat, message):
    """ 
        This one is mine :)))
        Don't even think about using it!
    """

    msg = re.sub('{} '.format(broadcast_command_w_msg), '', message.text)

    chats = get_users()
    for user in chats:
        bot.chat(user.get("chat_id")).send(msg)


broadcast_command_wo_msg = config("broadcast_command_wo_msg")
@bot.message_contains(broadcast_command_wo_msg)
def broadcast_hardcode_message(chat, message):
    """ 
        This one is mine :)))
        Don't even think about using it!
    """

    msg = """
        put your message here
    """

    chats = get_users()
    for user in chats:
        bot.chat(user.get("chat_id")).send(msg)


def get_users() -> list:
    return list(users.find(projection={"chat_id": 1, "_id": 0}))


if __name__ == "__main__":
    bot.run()
