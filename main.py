import os
import requests
from bs4 import BeautifulSoup
import telebot
from dotenv import load_dotenv

# Завантажуємо змінні оточення
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def get_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = soup.select(".titleline > a")[:5]  # Беремо перші 5 новин
    news_list = [f"{idx+1}. {article.text} - {article['href']}" for idx, article in enumerate(articles)]
    
    return "\n".join(news_list)

def send_news():
    news = get_news()
    if news:
        bot.send_message(CHAT_ID, f"📰 Останні новини:\n{news}")
    else:
        bot.send_message(CHAT_ID, "Не вдалося отримати новини.")

if __name__ == "__main__":
    send_news()
