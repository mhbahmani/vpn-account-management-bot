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
    try:
        users.insert_one(new_user)
        msg = """
سلام {}!!!
چطوری جون دل!؟ سر کیفی عزیز!؟؟ کیفت کوکه، بدم کوکه، بی‌خودی ادا حال بدارو در نیاااار!


تمام خدمات تابع قوانین جمهوری اسلامی ایران است🇮🇷
 تنها راه نجات = اطاعت از رهبری
 این پیروزیییییییییی، خسجته باد این پیروزیییییییییییییییییییی🥳
        """.format(new_user.get("first_name", "عزیز"))
    except pymongo.errors.DuplicateKeyError:
        msg = """
یه بار استارتو زدی دیگه. برو خونتون🚶🏻‍♂️
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


@bot.command("protocols")
def spam_command(chat, message, args):
    """Get setup guide"""
    btns = botogram.Buttons()
    btns[0].callback("ShadowsocskR", "ssr")

    chat.send("Choose a protocol to see how to setup", attach=btns)


@bot.callback("ssr")
def delete_callback(query, chat, message):
    ssr_msg = """
عمو بهمن شب جمعه‌ای با یه پروتکل جدید اومده. این دیگه تهشه. هر کی با این نتونه وصل شه، باید جمع کنه از ایران بره :))) ولی جدا از شوخی این کامل امتحانش رو پس داده، رو همه‌ی ispها هم کار می‌کنه.
برا اندروید اینو نصب کنید.
(https://play.google.com/store/apps/details?id=com.scala.ssr&hl=en&gl=US)
آیواس این:
 (https://apps.apple.com/us/app/potatso-2/id1162704202)
:ویندوز
 (https://github.com/shadowsocksrr/shadowsocksr-csharp/releases/download/4.9.2/ShadowsocksR-win-4.9.2.zip)
 :مک‌اوس
 (https://github.com/ShadowsocksR-Live/ssrMac/releases/download/0.6.2/ssrMac.app.zip)
 :لینوکس   تو ReadMe کامل توضیح داده،‌یه فایل کانفیگ می‌سازه، باید برید اونو عوض کنید.
 (https://github.com/ZoeyWoohoo/shadowsocksr):‌
 
{
    "server":"46.4.161.120",
    "server_port":17870,
    "local_address": "127.0.0.1",
    "local_port":1090,
    "password":"sagToFiltering",
    "timeout":300,
    "method":"chacha20-ietf",
    "protocol": "auth_chain_a",
    "obfs": "tls1.2_ticket_auth",
    "fast_open": true,
    "workers": 2
}

تو کلاینتتون، ببینید هر کدوم از این فیلدارو دارید پر کنید، بقیرم ایگنور کنید.

پ.ن.: این خداست، برید تستش کنید حتما.
پ.ن.۲: من لینوکس و اندرویدش رو تست کردم، اگه مشکل خوردید بگید روال کنیم
    """
    chat.send(ssr_msg)



def get_users() -> list:
    return list(users.find(projection={"chat_id": 1, "_id": 0}))


if __name__ == "__main__":
    bot.run()
