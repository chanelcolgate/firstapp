import feedparser
import paho.mqtt.client as mqtt
import time

#mqtt
mqtthost = "40.81.27.10"
mqttuser = "8fe579d0-e59d-4b58-9d47-0ada346b60a4:d8ee10e9-c01d-4970-a5bf-1aa7b5b8f882"
mqttpass = "bewBFfQO0SC9cL4PGlkLkt2kI"

# mongodb
client = pymongo.MongoClient('')
db = client['']

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

# mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/hello")
    print('subscribe on /hello')

def on_message(client, userdata, msg):
    print(msg.topic+','+msg.payload.decode())

    ti = datetime.datetime.now()
    topic = msg.topic
    data = msg.payload.decode()
    temp_id = collection.insert({'date':ti, 'topic': topic, 'data': data})
    new_temp = collection.find_one({'_id': temp_id})
    output = {'date': new_temp['date'],
            'topic': new_temp['topic'], 'data': new_temp['data']}
    print(output)

client = mqtt.Client()
client.username_pw_set(mqttuser, mqttpass)
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtthost, 1883, 60)
client.loop_start()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
