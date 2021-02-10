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
    """Just a simple start""""
    new_user = {"chat_id": chat.id,
                "username": chat.username,
                "first_name": chat.first_name,
                "last_name": chat.last_name}
    try:
        users.insert_one(new_user)
        msg = """
سلام {}!!!
چطوری جون دل!؟ سر کیفی عزیز!؟؟ کیفت کوکه، بدم کوکه، بی‌خودی ادا حال بدارو در نیاااار!
یه /help بزن تا ببینی با این بات زیبا چیکار می‌تونی بکنی


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
    btns[1].callback("OpenConnect", "openconnect")

    chat.send("Choose a protocol to see how to setup", attach=btns)


@bot.callback("ssr")
def ssr_callback(query, chat, message):
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
 
[
    "server": "{}",
    "server_port": {},
    "local_address": "127.0.0.1",
    "local_port":1090,
    "password": "{}",
    "timeout":300,
    "method": "{}",
    "protocol": "{}",
    "obfs": "{}",
    "fast_open": true,
    "workers": 2
]

تو کلاینتتون، ببینید هر کدوم از این فیلدارو دارید پر کنید، بقیرم ایگنور کنید.

پ.ن.: این خداست، برید تستش کنید حتما.
پ.ن.۲: من لینوکس و اندرویدش رو تست کردم، اگه مشکل خوردید بگید روال کنیم
    """.format(config('SERVER_IP'), config('SSR_PORT'), 
                config('SSR_PASSWORD'), config('SSR_METHOD'),
                config('SSR_PROTOCOL'), config('SSR_OBFS'))
    chat.send(ssr_msg)

@bot.callback("openconnect")
def openconnect_callback(query, chat, message):
    oc_msg = """
خوشگلای تو خونه، یه پروتکل جدید داریم. البته این یکی وی‌پی‌ان‌عه و مثه قبلیا پروکسی نیست.
خوشگلای قری لینوکسی، بای‌دیفالت اوپن‌کانکت ساپورت می‌کنه لینوکس و نیاز نیست چیزی نصب کنید، اگه نداره احیانا، این‌جا کامند نصبش هست.
https://people.eng.unimelb.edu.au/lucasjb/archive/oc_old.html
 بعد این که نصب کردید، میرید تو Settings > Network. اونجا یه VPN جدید می‌سازید و اطلاعات رو وارد می‌کنید. تو همون لینکه یه چیزایی گفته، البته خیلی قدیمیه و یه ذره فرق کرده الان لینوکس. ولی کلیت همونه.

عزیزای ویندوزی، ضمن این که سگ تو ویندوز، لینک اولی آموزش کامل هست، برید ببینید. کلاینتی هم که باید دانلود کنید رو از لینک دوم می‌تونید بگیرید.
https://openconnect.github.io/openconnect-gui/
https://github.com/openconnect/openconnect-gui/releases


اندرویدیای عزیز هم لینک اولو بمالن، اپ رو نصب کنن. آموزش هم تو لینک دوم هست.
https://play.google.com/store/apps/details?id=com.github.digitalsoftwaresolutions.openconnect&hl=en&gl=US
https://support.onevpn.com/android-openconnect

اینم واسه ios:
https://apps.apple.com/de/app/openvpn-connect/id590379981

اطلاعات وی‌پی‌ان هم اینه:
gateway/server ip : {}
username: {}
password: {}
هر چی غیر اینا بود خالی بذارید‌ :))

پ.ن.: توصیه می‌کنم از shadowsocksr استفاده کنید. نکته‌ی مثبت این اینه که وی‌پی‌انه و برای ویس کال و ویس چت تلگرام میشه ازش استفاده کرد.
    """.format(config('SERVER_IP'), config('OC_USERNAME'), config('OC_PASSWORD'))
    chat.send(oc_msg)


def get_users() -> list:
    return list(users.find(projection={"chat_id": 1, "_id": 0}))


if __name__ == "__main__":
    bot.run()
