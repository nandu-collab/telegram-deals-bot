import os
import feedparser
import telebot
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")
RSS_FEEDS = [
    "https://www.desidime.com/rss/lofre.json",
]

bot = telebot.TeleBot(BOT_TOKEN)

def fetch_and_post():
    posted_links = set()
    while True:
        for url in RSS_FEEDS:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                if entry.link not in posted_links:
                    message = f"**{entry.title}**\n{entry.link}"
                    bot.send_message(CHANNEL_USERNAME, message, parse_mode='Markdown')
                    posted_links.add(entry.link)
        time.sleep(900)

if __name__ == "__main__":
    fetch_and_post()
# telegram-deals-bot
