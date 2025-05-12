   import telebot

   TOKEN = 7764559021:AAFVlk4hE3bzbGGohIX0-Heu9sqk9OZALFg
   bot = telebot.TeleBot(TOKEN)

   goods = [
       "z11xer.t.me",
       "z111xer.t.me",
       "ziiixer.t.me",
       "bogxyev.t.me",
       "bogpipisek.t.me",
       "mrxyesosov.t.me",
       "apectoban_mamoi.t.me",
       "arectovan_swagom.t.me",
       "arectovan_za_swagu.t.me"
   ]

   @bot.message_handler(commands=['start'])
   def send_welcome(message):
       welcome = "сап это магаз rezyyy. лс для покупки the_rezyyy.t.me"
       bot.send_message(message.chat.id, welcome)
       bot.send_message(message.chat.id, '\n'.join(goods))

   bot.infinity_polling()
