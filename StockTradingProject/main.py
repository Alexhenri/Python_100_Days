import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def has_sharp_increase_or_decrease() -> (float, bool):
    stock_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": STOCK,
        "outputsize": "compact",
        "apikey": "8KEOWV05PLY8DK3R"
    }
    response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
    response.raise_for_status()
    stock_json = response.json()
    stock_data = stock_json["Time Series (Daily)"]
    yesterday_stock_info = list(stock_data.values())[0]

    yesterday_open = float(yesterday_stock_info["1. open"])
    yesterday_close = float(yesterday_stock_info["4. close"])
    percentage = ((yesterday_open - yesterday_close) / yesterday_open) * 100
    if abs(percentage) >= 1:
        return percentage, True
    else:
        return percentage, False


def send_sms_alert(msg):
    account_sid = "AC50f7647b4b67dd5c347da799846ed596"
    auth_token = "2cef1240f2e7ffa994e0719ca73966e0"
    # auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=msg,
        from_="+13614268205",
        to="MY_NUMBER_HERE"
    )
    print(message.status)


def get_news():
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": "b0e0659af92c456eaac259f748409da8",
        "sortBy": "popularity",
        "pageSize": "3"
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    response.raise_for_status()
    news_json = response.json()
    articles = news_json["articles"]
    formatted_articles = []
    for article in articles:
        formatted_articles.append((article['title'], article['description'] ))

    return formatted_articles


pct, need_alert = has_sharp_increase_or_decrease()
if need_alert:
    news = get_news()
    for new in news:
        msg = f"Headline: {new[0]}\nBrief: {new[1]}\n\n"
        body_msg = f"{STOCK}: {round(pct, 2)}\n{new}"
    send_sms_alert(body_msg)
