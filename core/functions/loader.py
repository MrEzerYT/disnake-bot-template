from os import listdir

def ModulesLoader(self):
    for filename in listdir("core/modules"):
        if filename.endswith(".py") and not filename.startswith("_"):
            try:
                self.load_extension(f"core.modules.{filename[:-3]}"); self.logger.success(f"Module {filename} is loaded!")
            except Exception as e:
                self.logger.error(f"Module {filename} fucked up: {e}")
    self.logger.success("All modules loaded!")