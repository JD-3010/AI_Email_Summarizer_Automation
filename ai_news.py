import feedparser

def get_ai_news():
    feed = feedparser.parse("https://www.technologyreview.com/feed/")
    news = []

    for entry in feed.entries[:5]:
        news.append(entry.title)

    return news
