from os import listdir, system; from pathlib import Path

def ModulesLoader(client):
    """
    Подгружает все cogs из директории core/modules.

    Для использования вам необходимо настроить logger от loguru и создать отдельный класс бота.
    """
    for module in listdir("core/modules"):
        if module.endswith(".py") and not module.startswith("_"):
            try:
                client.load_extension(f"core.modules.{module[:-3]}"); client.logger.success(f"» Module {module} is loaded!")
            except Exception as e:
                client.logger.error(f"» Module {module} fucked up: {e}")
    client.logger.success("All modules loaded!")