import yaml


class Config:
    def __init__(self):
        self.configfile = "config.yaml"

    def parseConfig(self):
        with open(self.configfile, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
