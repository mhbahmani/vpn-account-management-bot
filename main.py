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

if __name__ == "__main__":
    bot.run()
