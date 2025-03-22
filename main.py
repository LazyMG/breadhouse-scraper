from data_scraper import fetch_data
from file_handler import save_to_file
from id_scraper import fetch_ids
from file_handler import save_test_id_to_txt, add_id_to_completed_id_text_file, update_id_list_text_file,get_id_from_id_list_text_file

import sys
sys.stdout.reconfigure(encoding='utf-8')

def main():
    # 반복문 필요
    id_list = get_id_from_id_list_text_file()
    # print(id_list)
    # 아이디를 파일에서 가져옴
    id = 10917  # 원하는 ID 값 설정

    for id in id_list:
      # 데이터 추출
      data = fetch_data(id)

      try:
        # 파일 저장
        save_to_file(data, id, data["date"])
      except:
        print("----json data error----")
        print(f"error id: {id}")
        print("-----------")

      try:
        # 정상적으로 가져온 아이디는 
        # 완료 아이디 파일에 저장하고
        # 기존 아이디 파일에서 삭제
        add_id_to_completed_id_text_file(id)
        update_id_list_text_file()
      except:
        print("----text file update error----")
        print(f"error id: {id}")
        print("-----------")

# 실행 예시
if __name__ == "__main__":
    # fetch_ids() # 주기적으로 업데이트 하기기

    # main()
    print("okay")