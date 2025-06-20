# 📰 Daily News Email Bot

A Python script that fetches the latest headlines from top global news outlets using RSS feeds and sends them to your email every day in a clean, formatted digest. Built to demonstrate real-world automation, email integration, and professional polish for your GitHub and LinkedIn profile.

---

## 📌 Features

- Pulls top headlines from:
  - [Reuters](https://www.reuters.com/)
  - [Al Jazeera](https://www.aljazeera.com/)
  - [BBC World News](https://www.bbc.com/news/world)
  - [The Hacker News](https://thehackernews.com/)
- Uses official RSS feeds for reliable data (no fragile scraping)
- Sends a beautifully formatted HTML email
- Built for automation (cron, GitHub Actions, VPS, etc.)
- Clean, professional code ready for production

---

## 📸 Screenshot

*Example of the email output:*

> 📰 **Daily News Digest – Monday, June 20, 2025**  
> - **BBC World:** [UN warns of food crisis in Sudan](https://www.bbc.co.uk/...)  
> - **Reuters:** [Oil prices rise amid tensions in the Gulf](https://www.reuters.com/...)  
> - *(...)*

---

## 🚀 Usage

### 1. Clone this repo
```bash
git clone https://github.com/your-username/daily-news-email-bot.git
cd daily-news-email-bot
