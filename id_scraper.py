import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv("BASE_URL")

from file_handler import save_id_to_txt, check_completed_id

start = 0
end = 75 # 기본 5페이지 탐색
CURRENT_LAST_PAGE = 6105 # 25년 3월 기준 총 페이지 수

def fetch_ids():  
  i = start
  while i <= end:
    response = requests.get(f"{base_url}?start={i}")
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.content, "html.parser")

    anchors = soup.find_all("td", class_="sel_maindblist")

    a_tags = [td.find("a") for td in anchors if td.find("a")]
    id_set = set()

    for a in a_tags:
        href = str(a.get("href"))
        id = href.split("id=")[1]
        id_set.add(id)

    id_list = list(id_set)
    id_list.sort(reverse=True)

    check_tuple = check_completed_id(id_list)

    save_id_to_txt(check_tuple[0])

    if check_tuple[1]:
      break
    
    i += 15