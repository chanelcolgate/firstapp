import feedparser
import paho.mqtt.client as mqtt
import time

mqtthost = "40.81.27.10"
mqttuser = "8fe579d0-e59d-4b58-9d47-0ada346b60a4:d8ee10e9-c01d-4970-a5bf-1aa7b5b8f882"
mqttpass = "bewBFfQO0SC9cL4PGlkLkt2kI"

from flask import Flask

app = Flask(__name__)

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml"

@app.route("/")
def get_news():
    feed = feedparser.parse(BBC_FEED)
    first_article = feed['entries'][0]
    return """<html>
        <body>
            <h1> BBC Headlines </h1>
            <b>{0}</b> <br/>
            <i>{1}</i> <br/>
            <p>{2}</p> <br/>
        </body>
</html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
