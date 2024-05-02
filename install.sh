#!/bin/bash

##############################################################################

clear
clear

printf "\n\n\e[3;34;40m Installing...\e[0m\n\n"

##############################################################################
echo "Installing..."

sudo apt update && apt upgrade
clear
apt install python3
apt install python3-pip
apt install screen
echo "Python3 успешно установлен, установка модулей бота"
cd disnake-bot-template
python3 -m pip install -r requirements.txt
clear
exit(0)
