from flask import Flask
import random

app = Flask(__name__)

gifs = [
        "https://media.giphy.com/media/yyZRSvISN1vvW/giphy.gif",
        "https://media.giphy.com/media/SFRhYgSElTfvG/giphy.gif",
        "https://media.giphy.com/media/l1L2UkgpuiE4U/giphy.gif",
        "https://media.giphy.com/media/119i1S64KnIhyM/giphy.gif",
        "https://media.giphy.com/media/l0MYwONBGDS7aPGOk/giphy.gif",
        "https://media.giphy.com/media/l3UcD7vkCptuTGAX6/giphy.gif",
        "https://media.giphy.com/media/3osxY7eI6enqNBo2mQ/giphy.gif",
        "https://media.giphy.com/media/oVQLjs0Ci6VJ6/giphy.gif",
        "https://media.giphy.com/media/qTd24wzmpiyis/giphy.gif",
        "https://media.giphy.com/media/3oeSAIKdl2WHKaUqIg/giphy.gif",
        "https://media.giphy.com/media/ef61oIGVyckY8/giphy.gif",
        "https://media.giphy.com/media/ZeB4HcMpsyDo4/giphy.gif",
        "https://media.giphy.com/media/goIcmbcUMEnyE/giphy.gif",
        "https://media.giphy.com/media/3ohs4BE3jdfEdneY0M/giphy.gif",
        "https://media.giphy.com/media/3o8doM1LK2PVaxawpO/giphy.gif",
        "https://media.giphy.com/media/NI8fT7ugMo9eU/giphy.gif",
        "https://media.giphy.com/media/4KZiHfMZIDbPi/giphy.gif",
        "https://media.giphy.com/media/JRQ1PegFVKXBu/giphy.gif",
        "https://media.giphy.com/media/EmSCxtcjQCmXK/giphy.gif",
        "https://media.giphy.com/media/1d6TZuzdBboDm/giphy.gif",
        "https://media.giphy.com/media/lmBV7ec6jRIPK/giphy.gif",
        "https://media.giphy.com/media/5mNhd8i7y7ygg/giphy.gif",
        ]

@app.route("/")
def main():
    gif = random.choice(gifs)
    return '<center><img src="{}"></center>'.format(gif)
