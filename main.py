from decouple import config
import botogram


bot = botogram.create(config("API_KEY"))


if __name__ == "__main__":
    bot.run()
