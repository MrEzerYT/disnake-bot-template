#!/bin/bash

sudo apt update && apt upgrade
apt install python3
apt install python3-pip
echo "Python3 успешно установлен, установка модулей бота"
python3 -m pip install -r requirements.txt
clear
echo "Установка завершена!"
exit(0)