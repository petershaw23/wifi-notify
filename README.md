# wifind-bot
telegram bot using nmap to find all mac addresses in local wifi / lan

## installation:

git clone https://github.com/petershaw23/wifind-bot/

`sudo pip3 install telepot` installs telepot / telegram library for python

`sudo pip3 install python-nmap` installs nmap library for python

`sudo apt install nmap` installs nmap. not sure if needed

## usage / setup:

edit the main script:

`cd wifind-bot`

`sudo nano wifind.py`


1. change "target_mac" in line 24.
2. change "hosts='192.168.**0**.0/24'" in line 66, if IP mask is _not_ 192.168.**0**.X. (192.168.**1**.X is also common)

save and close the file.


create a telegram bot, instructions here:

https://core.telegram.org/bots#3-how-do-i-create-a-bot

note the secret bot token-key.

create the 2 config files "pibot-token.py" and "IDList.py" in same directory as wifind.py:



create token config file:

`sudo nano pibot-token.py`


content:

`token = "xxxx"` insert telegram bot token-key here

save and close the file.

create ID list config file:

`sudo nano IDList.py`

content:

`IDList = [xxxxxx, xxxxxx, ...]` insert telegram IDs, that are allowed to use the bot, here. multiple IDs separated by commas

(how to find your telegram ID: https://www.alphr.com/telegram-find-user-id/, or start the bot without entering any vaild IDs, then read the python output after sending a message to the bot. the python output will show your telegram ID)

save and close the file.



`sudo python3 wifind.py` starts the bot with _root_ privileges, without root privileges nmap cannot find MAC addresses!
