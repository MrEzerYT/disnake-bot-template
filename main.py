from core.config import Status; from core.libs import *

@client.event
async def on_ready():
    await status.start()

@loop(seconds=60.0)
async def status():
    current_status = choice(Status)
    await client.change_presence(activity=Game(name=current_status, platform="Linux"))

if __name__ == "__main__":
    try:
        client.run(token)
    except Exception as e:
        client.logger.warning('При запуске произшла непредвиденная ошибка!')
        client.logger.exception(f'Ошибка: {e}')