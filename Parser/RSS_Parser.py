import feedparser

def getLastArticleAll(feed):
    x = 0
    feed = feedparser.parse(feed)
    for article in feed['entries']:
        for m in article['links']:
            href = (m['href'])
            x += 1
        if x == 1:
            return href

if __name__ == '__main__':
    getLastArticleAll("https://habr.com/ru/rss/flows/design/all/?fl=ru")