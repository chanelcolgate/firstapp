import feedparser


from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
        'cnn': 'http://rss.cnn.com/rss/edition.rss',
        'fox': 'http://feeds.foxnews.com/foxnews/latest',
        'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
@app.route("/bbc")
def bbc():
    return get_news('bbc')

@app.route("/cnn")
def cnn():
    return get_news('cnn')

@app.route("/fox")
def fox():
    return get_news('fox')

@app.route('/iol')
def iol():
    return get_news('iol')

def get_news(publication):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][1]
    return render_template("home.html",
            title=first_article.get("title"),
            published=first_article.get("published"),
            summary=first_article.get("summary"))    

if __name__ == '__main__':
    app.run(port=5000, debug=True)
