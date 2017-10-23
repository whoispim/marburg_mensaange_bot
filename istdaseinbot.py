from telegram.ext import Updater
from telegram.ext import CommandHandler
from configparser import SafeConfigParser
import subprocess
import re

config = SafeConfigParser()
config.read("ident.ini")

updater = Updater(token=config.get("API","token"))
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Es ist angerichtet!")

def mensa(bot, update):
    raw, err = subprocess.Popen(['./oneliner.sh'], stdout=subprocess.PIPE).communicate()
    
    blue = raw.decode("utf-8")
    
    menuint = 0
    rare = []
    rare.append("")
    
    out = ""

    for line in blue.splitlines():
        if line != " ":
            rare[menuint] = rare[menuint] + line + " "
        else:
            menuint += 1
            rare.append("")
    
    rare = rare[:-1]
    
    boese = ['12','13','17','18','19','22','29','Rind','rind','Pute','pute','Huhn','huhn','Hähn','hähn','geflügel','Geflügel','chicken','Chicken']
    
    for gericht in rare:
        if any (x in gericht for x in boese):
            out = out + "💔 " + gericht + "\n"
        else:
            out = out + "💚 " + gericht + "\n"
    if out == "":
        out = "¯\_(ツ)_/¯"
    bot.send_message(chat_id=update.message.chat_id, text=out)



def ohnebeilagen(bot, update):
    raw, err = subprocess.Popen(['./oneliner.sh'], stdout=subprocess.PIPE).communicate()
    
    blue = raw.decode("utf-8")
    
    menuint = 0
    rare = []
    rare.append("")
    
    out = ""

    for line in blue.splitlines():
        if line != " ":
            rare[menuint] = rare[menuint] + line + " "
        else:
            menuint += 1
            rare.append("")
    
    rare = rare[:-1]
    
    boese = ['12','13','17','18','19','22','29','Rind','rind','Pute','pute','Huhn','huhn','Hähn','hähn','geflügel','Geflügel','chicken','Chicken']
    
    for gericht in rare:
        if any (x in gericht for x in boese):
            out = out + "💔 " + gericht + "\n"
        else:
            out = out + "💚 " + gericht + "\n"
    out = re.sub(r' \(.+?\)','',out)
    if out == "":
        out = "¯\_(ツ)_/¯"
    bot.send_message(chat_id=update.message.chat_id, text=out)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

mensa_handler = CommandHandler('essen', mensa)
dispatcher.add_handler(mensa_handler)

ohnebeilagen_handler = CommandHandler('ohne_beilagen', ohnebeilagen)
dispatcher.add_handler(ohnebeilagen_handler)

updater.start_polling()


