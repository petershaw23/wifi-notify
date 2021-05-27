# wifind-bot
telegram bot using nmap to find all mac addresses in local wifi / lan

## installation:

git clone https://github.com/petershaw23/wifind-bot/

`sudo pip3 install telepot` installs telepot library for python

`sudo pip3 install python-nmap` installs nmap library for python

`sudo apt install nmap` installs nmap. not sure if needed

## usage:

create a telegram bot, instructions here:

https://core.telegram.org/bots#3-how-do-i-create-a-bot

create the 2 config files in same directory as wifind.py:

`sudo nano pibot-token.py`

content:

`token = "xxxx" #insert telegram bot token here`


`sudo nano IDList.py`

content:

`IDList = [xxxxxx, xxxxxx, ...] #insert telegram IDs, that are allowed to use the bot, here.`

how to find your telegram ID: https://www.alphr.com/telegram-find-user-id/

`sudo python3 wifind.py` start the bot with root privileges, otherwise nmap cannot find MAC addresses.
