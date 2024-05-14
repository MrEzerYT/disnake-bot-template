from os import listdir; from pathlib import Path

def ModulesLoader(client, path):
    """
    Подгружает все cogs из директории core/modules.

    Для использования вам необходимо настроить logger от loguru и создать отдельный класс бота.
    """
    if Path(path).exists():
        client.logger.debug(f"Directory {path} exists!")
    else:
        Path(path).mkdir(parents=True, exist_ok=False)
        client.logger.debug(f"Directory {path} was created!")
    for module in listdir(path):
        if module.endswith(".py") and not module.startswith("_"):
            try:
                client.load_extension(f"core.modules.{module[:-3]}"); client.logger.success(f"» Module {module} is loaded!")
            except Exception as e:
                client.logger.error(f"» Module {module} fucked up: {e}")
    client.logger.success("All modules loaded!")
