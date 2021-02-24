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
    """Just a simple start"""
    new_user = {"chat_id": chat.id,
                "username": chat.username,
                "first_name": chat.first_name,
                "last_name": chat.last_name}
    try:
        users.insert_one(new_user)
        send_msg_to_admin('{} just started the bot'.format(new_user.get('username', 'Some one')))
        msg = """
سلام {}!!!
چطوری جون دل!؟ سر کیفی عزیز!؟؟ کیفت کوکه، بدم کوکه، بی‌خودی ادا حال بدارو در نیاااار!
یه /help بزن تا ببینی با این بات زیبا چیکار می‌تونی بکنی


تمام خدمات تابع قوانین جمهوری اسلامی ایران است🇮🇷
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
    btns[2].callback("SSH (SOCKS5 Proxy)", "ssh")
    btns[3].callback("Shadowsocks", "ss")

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


@bot.callback("ssh")
def ssh_callback(query, chat, message):
    oc_msg = """
یه کاری که میشه کرد، اینه که به سرور اسسچ زد. با این کامنده، یه پروکسی socks5 رو سیستمتون می‌سازه. همه‌ی سیستم‌عامل‌ها هم اوکین.
ssh -D 1080 {}@{}

برای این که بتونید از این استفاده کنید، باید ssh keyتون رو برام بفرستید که به سرور ادد کنم. تو لینوکس اینو بزنید بهتون میدتش.
cat ~/.ssh/id_rsa.pub
خروجیش رو کپی کنید و برام بفرستید. تو ویندوز هیچ ایده‌ای ندارم چطوریه.

اینم یه راهنمای ریز برای این که چطوری یه public key بسازید اگه ندارید:
1- Type ssh in terminal to make sure ssh is installed.
2- Create ssh public key in your client by ssh-keygen -t rsa
* If you want to add your email, use this command ssh-keygen -t rsa -C "your_email@example.com"
    """.format(config('SSH_USER'), config('SERVER_IP'))
    chat.send(oc_msg)


@bot.callback("ss")
def ss_callback(query, chat, message):
    oc_msg = """
https://shadowsocks.org/en/download/clients.html
از این‌جا، برید برای هر چی که می‌خواید یه کلاینت دانلود کنید.
من فقط لینوکس و اندرویدش رو استفاده کردم، توی لینوکس، این از همه بهتر بود:
https://github.com/shadowsocks/shadowsocks-qt5/wiki/Installation
اندروید هم این:
https://play.google.com/store/apps/details?id=com.github.shadowsocks
اونی که برای لینوکسه، خودش گفته چطوری باید رانش کنید. می‌تونید کامندش رو بذارید توی استارتاپ تا هر وقت میاد بالا لینوکس بازش کنه براتون.

حالا بعد این که دانلود کردید کلاینتتون رو، باید اینارو توش کانفیگ کنید. مشخصاتی که می‌خواید ایناست:
server: {}
port: {}
pass: {}
method: {}

لوکال آدرس و لوکال پورت هم خودش ست شده یحتمل، btw اگه نشده بود:
local address: 127.0.0.1
local port: 1080
پورت رو هر چی دوست دارید می‌تونید بذارید.

عز آلویز، پخش نکنید اینارو، به خانواده اوکیه.
    """.format(config('SERVER_IP'), config('SS_PORT'), config('SS_PASSWORD'), config('SS_METHOD'))
    chat.send(oc_msg)


def send_msg_to_admin(msg):
    admin = get_admin()
    if admin:
        bot.chat(admin).send(msg)


def get_admin():
    admin = db.users.find_one(
            filter={'username': re.sub('@', '', bot.owner)},
            projection={'_id': 0, 'chat_id': 1})
    return admin.get('chat_id', None)


def get_users() -> list:
    return list(users.find(projection={"chat_id": 1, "_id": 0}))


if __name__ == "__main__":
    bot.run()
