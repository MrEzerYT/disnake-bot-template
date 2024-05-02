# Основа бота для мессенджера Discord.

Это что-то типо шаблона для бота (то, что я считаю важным в начальном создании бота). <br>
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
## Authors

- [@MrEzerYT](https://www.github.com/MrEzerYT)

## Features

- Легкое добавление модуля с командами/функциями 
- Гибкое управление в конфигурации
- Поддержка любой платформы
- Кастомизация статуса
- Поддержка со стороны разработчика

## To do
- [x] Оформить README
- [x] Переписать бота
- [x] Изменение статуса в конфигурации
- [ ] Конфигурация в JSON формате для изменения конфигурации путем ввода команд
- [x] Тикеты
- [x] Гибкая настройка в конфигурации
- [x] Скрипт автоматической установки панели на сервер Linux (Ubuntu, Kali, Debian)
- [x] Система логирования
- [ ] Отправка ошибок в директорию errors и Discord канал с подробной информацией
- [ ] Готовые модули для кастомизации (Статус Minecraft сервера, локаций в Pterodactyl и т.д.)

## Installation

Установка на Linux (скоро будут фиксы скрипта)

```bash
  git clone https://github.com/MrEzerYT/disnake-bot-template.git bot
  cd bot
  bash install.sh && rm -rf install.sh
```

Запуск:

```bash
cd bot
screen -dmS bot python3 -m main.py
```
