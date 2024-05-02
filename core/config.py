prefix = "."

class Auth:
    discord_auth = {
        "debug" : "", # Токен с сайта discord.com/developers тут указывается тестовый бот
        "release" : "" # Токен с сайта discord.com/developers тут указывается рабочий бот
    }


Status = [f'{prefix}help | flyrix.space',
          'разработчик: @mrezer',] # можете добавить любой статус, он будет ставиться на рандом в main.py

class Config:
    yoomoney_id = 4100118214101291 # https://yoomoney.ru/settings
    support_role_id = ""  # id роли поддержки. Например, 1231516556589006899
    footer_text = "🐋 disnake-bot-template » https://github.com/MrEzerYT/disnake-bot-template"