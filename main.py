from core.libs import *

if __name__ == "__main__":
    try:
        client.run(token)
    except Exception as e:
        client.logger.warning('При запуске произшла непредвиденная ошибка!') # скоро добавлю типы ошибок, т.к. это будет удобнее для вас
        client.logger.exception(f'Ошибка: {e}')