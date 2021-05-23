# Telegram bot Wifi Scanner, scannt nach MAC adresse mit nmap
# abhängigkeiten:
# sudo pip3 install python-nmap
# sudo pip3 install telepot
# wichtig: mit "sudo python3 wifind.py" starten, sonst findet er keine MAC adressen

from time import sleep
import os
import nmap
import subprocess
import time
import datetime 
import telepot
from telepot.loop import MessageLoop    # Library function to communicate with telegram bot

#print(os.environ) #test 

import pibot_token # imports local file pibot-token.py with telegram bot token. content: token = "xxxx"
token = pibot_token.token
import IDList # imports local file IDList.py with allowed telegram users. content: IDList = [xxxxxx, xxxxxx, ...]
IDList = IDList.IDList


target_mac = "B0:2A:43:FC:19:2F" #hier die mac adresse vom ziel eintragen

   
def handle(msg):
    
    def logging(status):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        print (str(timestamp) +': '+str(command)+' sent by telegram user ID# '+str(sender)+': '+str(status))
    
    
    chat_id = msg['chat']['id']
    command = msg['text']
    sender = msg['from']['id']
    
    if sender in IDList:
        logging('allowed!')

 
        if command == '/start':
            bot.sendMessage (chat_id, str("Hi!"))
        elif command == '/time':
            now = datetime.datetime.now() # Getting date and time
            bot.sendMessage(chat_id, str(now.hour) + str(":") + str(now.minute), parse_mode= 'Markdown')
        elif command == '/date':
             now = datetime.datetime.now() # Getting date and time
             bot.sendMessage(chat_id, str("Date: ") + str(now.day) + str("/") + str(now.month) + str("/") + str(now.year))

        elif command == '/uptime':
            with open('/proc/uptime', 'r') as f:
                seconds = float(f.readline().split()[0])
            day = seconds // (24 * 3600)
            seconds = seconds % (24 * 3600)
            hour = seconds / 3600
            seconds %= 3600
            minutes = seconds //60
            seconds %= 60
            seconds2 = seconds
            timeformat = "d:h:m:s   %d:%d:%d:%d" % (day, hour, minutes, seconds2)
            bot.sendMessage(chat_id, timeformat)
        elif command == '/wifi':
            bot.sendMessage(chat_id, str("scanning..."))
            nm = nmap.PortScanner()
            nm.scan(hosts='192.168.0.0/24', arguments='-sP') #hier die IP range eingeben, kann auch z.B. 192.168.1.0/24 sein
            host_list = nm.all_hosts()
            print(host_list)
            bot.sendMessage(chat_id, str("Liste der gefundenen Geräte:"))
            for host in host_list:
                if 'mac' in nm[host]['addresses']:
                    print(host+' : '+nm[host]['addresses']['mac'])
                    bot.sendMessage(chat_id, (host+' : '+nm[host]['addresses']['mac']))
                    if target_mac == nm[host]['addresses']['mac']:
                        print('Target Found') 
                        bot.sendMessage(chat_id, str("*Target ") + target_mac + str(" found!*"), parse_mode= 'Markdown')

    else:
        bot.sendMessage(chat_id, 'access denied! you suck, telegram user ID# '+str(sender))
        logging('DENIED!')

bot = telepot.Bot(token) # get token key from from local file pibot-token.py
print (bot.getMe())

# Start listening to the telegram bot and whenever a message is  received, the handle function will be called.
MessageLoop(bot, handle).run_as_thread()
print ('Listening....')

while 1:
    sleep(10)

