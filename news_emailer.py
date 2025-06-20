#!/usr/bin/env python3
# Daily News RSS Email Bot
# Author: Jerad Zackuse

import feedparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
from datetime import datetime

# ------------------------ CONFIG ------------------------

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

GMAIL_USER = "youremail@gmail.com"
GMAIL_PASS = "your app password. not gmail sign in password"
RECIPIENT = "youremail@gmail.com"

NEWS_FEEDS = {
    "Reuters": "http://feeds.reuters.com/reuters/topNews",
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "Cybersecurity News": "https://feeds.feedburner.com/TheHackersNews",
    "BBC World": "http://feeds.bbci.co.uk/news/world/rss.xml"
}


# ------------------------ PARSE FEEDS ------------------------

def fetch_headlines():
    headlines = []

    for source, feed_url in NEWS_FEEDS.items():
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:5]:
                title = entry.title
                link = entry.link
                headlines.append((source, title, link))
        except Exception as e:
            headlines.append((source, f"Error reading feed: {e}", feed_url))

    return headlines

# ------------------------ FORMAT EMAIL ------------------------

def create_email_content(headlines):
    date_str = datetime.now().strftime("%A, %B %d, %Y")
    html = f"<h2>📰 Daily News Digest – {date_str}</h2><ul style='font-size:15px;'>"

    for source, title, link in headlines:
        html += f'<li><strong>{source}:</strong> <a href="{link}" target="_blank">{title}</a></li>'

    html += "</ul><p style='font-size:12px; color:gray;'>Sent automatically by your Python bot 📬</p>"
    return html

# ------------------------ SEND EMAIL ------------------------

def send_email(html_content):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "🌍 Your Daily News Brief"
    msg["From"] = GMAIL_USER
    msg["To"] = RECIPIENT

    msg.attach(MIMEText(html_content, "html"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(GMAIL_USER, GMAIL_PASS)
        server.send_message(msg)

# ------------------------ MAIN ------------------------

def main():
    print("[+] Fetching news from RSS feeds...")
    headlines = fetch_headlines()
    print(f"[+] Retrieved {len(headlines)} total articles.")

    print("[+] Formatting email...")
    html = create_email_content(headlines)

    print("[+] Sending email...")
    send_email(html)

    print("[✔] Done. Email sent!")

if __name__ == "__main__":
    main()
