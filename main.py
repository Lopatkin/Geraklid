# -*- coding: utf-8 -*-

import telebot
import constants
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

bot = telebot.TeleBot(constants.token)

#   bot.send_message(859320, 'привет')

print (bot.get_me())

def log(message, answer):
    print ("\n -----")
    from datetime import datetime
    print (datetime.now())
    print ("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                    message.from_user.last_name,
                                                                    str(message.from_user.id),
                                                                    message.text))
    print (" Ответ - " + answer)



@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Привет":
        answer = "Привет, человек"
        bot.send_message(message.chat.id, answer)
        log(message, answer)
    else:
        answer = "Ответа нет"
        log(message, answer)






bot.polling(none_stop=True, interval=0)
