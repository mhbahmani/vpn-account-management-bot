from decouple import config
import botogram


bot = botogram.create(config("API_KEY"))
bot.about = config("about")
bot.owner = config("owner")


if __name__ == "__main__":
    bot.run()
