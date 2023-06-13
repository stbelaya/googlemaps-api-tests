import os


# $Env:ENV='dev' or $Env:ENV='prod'
class Environment:
    DEV = 'dev'
    PROD = 'prod'
    KEY = "?key=qaclick123"

    URLS = {
        PROD: "https://rahulshettyacademy.com"
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.PROD

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")


ENV_OBJECT = Environment()
