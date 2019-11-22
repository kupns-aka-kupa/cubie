from app import App
from conf import Config

conf = Config()
app = App(conf)

app.init()
app.update()
