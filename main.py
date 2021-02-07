from decouple import config
import botogram
import pymongo
from pymongo import MongoClient


bot = botogram.create(config("API_KEY"))
bot.about = config("about")
bot.owner = config("owner")

client = MongoClient()
db = client.vpnbotdb
users = db.users


@bot.command("start")
def add_user(chat, message, args):
    new_user = {"chat_id": chat.id}
    users.insert_one(new_user)
    chat.send("Welcome to booooooooooo bot!")


@bot.message_contains("sendthistoall")
def broadcast_command(chat, message):
    """ 
        This one is mine :)))
        Don't even think about using it!
    """

    chats = get_users()
    for user in chats:
        bot.chat(user.get("chat_id")).send("yes")


def get_users() -> list:
    return list(users.find(projection={"chat_id": 1, "_id": 0}))


if __name__ == "__main__":
    bot.run()
