import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL")

def fetch_data(id):
    url = f'{base_url}?id={id}'
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.content, "html.parser")
    
    year_content = soup.find("div", class_="text1").get_text(strip=True)
    day = soup.find("div", class_="text2").get_text(strip=True)
    day_content = day.split("/")
    date = f"{year_content}-{day_content[0]}-{day_content[1]}"
    
    range_and_title = soup.find_all("span", class_="ng_title")
    range_content = range_and_title[0].find("a").get_text(strip=True)
    title = range_and_title[1].get_text(strip=True)
    
    message_and_application_and_oneline = soup.find_all("div", class_="ng_tdbbody2")
    message = message_and_application_and_oneline[0].get_text(strip=True)
    
    verse_texts = [verse.get_text(strip=True) for verse in soup.find_all("td", class_="ng_tdbbody1")]
    verse_list = [{"index": verse_texts[i], "content": verse_texts[i + 1]} for i in range(0, len(verse_texts), 2)]
    
    application_and_oneline = message_and_application_and_oneline[1:]
    application = application_and_oneline[0].get_text(strip=True)
    oneline = application_and_oneline[1].get_text(strip=True)
    
    data = {
        "id": str(id),
        "date": date,
        "title": title,
        "range": range_content,
        "verses": verse_list,
        "message": message,
        "application": application,
        "oneline": oneline
    }
    
    return data