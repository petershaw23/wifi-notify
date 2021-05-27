# wifind-bot
telegram bot using nmap to find all mac addresses in local wifi / lan

## installation:

git clone https://github.com/petershaw23/wifind-bot/

`sudo pip3 install telepot` installs telepot / telegram library for python

`sudo pip3 install python-nmap` installs nmap library for python

`sudo apt install nmap` installs nmap. not sure if needed

## usage:

create a telegram bot, instructions here:

https://core.telegram.org/bots#3-how-do-i-create-a-bot

note the secret bot token-key.

create the 2 config files "pibot-token.py" and "IDList.py" in same directory as wifind.py:

first config file:

`sudo nano pibot-token.py`


content:

`token = "xxxx"` insert telegram bot token-key here

save and close the file.

create 2nd config file:

`sudo nano IDList.py`

content:

`IDList = [xxxxxx, xxxxxx, ...]` insert telegram IDs, that are allowed to use the bot, here. multiple IDs separated by commas

(how to find your telegram ID: https://www.alphr.com/telegram-find-user-id/, or start the bot without entering any IDs, and read the output after sending a message to the bot)

save and close the file.



`sudo python3 wifind.py` starts the bot with _root_ privileges, without root privileges nmap cannot find MAC addresses!
