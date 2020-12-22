from shop.bot.server_bot import bot, app
import time
from shop.bot import config

bot.remove_webhook()
time.sleep(0.5)
bot.set_webhook(config.WEBHOOK_URL, certificate=open('webhook_cert.pem'))
app.run()
