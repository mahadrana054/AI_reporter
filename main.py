import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

print("__Welcome to pakupdates.ai__")
name_user = input("Enter your name :")
load_dotenv(override=True)
api_key = os.getenv("NEWS_API_KEY")

if api_key is None or api_key == "":
    print("❌ API key not found!")
    print("\n📋 How to fix this:")
    print("1. Open Command Prompt (Windows) or Terminal (Mac/Linux)")
    print("2. Type: set NEWS_API_KEY=your_api_key_here  (Windows)")
    print("   Or type: export NEWS_API_KEY=your_api_key_here  (Mac/Linux)")
    print("3. Replace 'your_api_key_here' with your actual NewsAPI key")
    print("4. Run this program again")
    print("\n💡 This keeps your API key secret and safe!")
    exit()
else:
    print("✅ API key found!")

news = input("What type of news ypu are interested :")

if news == "" or news == " ":
    print("❌ Oops! You didn't type anything. Please run the program again and enter a topic.")

print(f"Getting latest news for  you {name_user}")
 
today = datetime.now()

past_date = today - timedelta(days = 1)

from_date = past_date.strftime('%Y-%m-%d')

print(f"📆 Searching from {from_date} to today ({today.strftime('%Y-%m-%d')})")

news_website = "https://newsapi.org/v2/everything"

web_address = f"{news_website}?q={news}&from={from_date}&sortBy=publishedAt&pageSize=5&apiKey={api_key}"

print(f"Searching for your {news} latest news...")

print(f"Please wait a moment...")

response = requests.get(web_address)

if response.status_code != 200:
    print(f"❌ Error fetching news! Status code: {response.status_code}")
    print("Message:", response.json().get("message", "Unknown error"))
    exit()

news_data = response.json()

articles = news_data.get("articles", [])
if not articles:
    print("⚠️ Sorry, no news found for your topic.")
else:
    print("📰 Here are the latest news articles:\n")
for i, article in enumerate(articles, start=1):
    print(f"{i}. {article['title']}")
    print(f"   Source: {article['source']['name']}")
    print(f"   Published: {article['publishedAt']}")
    print(f"   URL: {article['url']}\n")






