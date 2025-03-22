import json
import os

from dotenv import load_dotenv

load_dotenv()

data_path = os.getenv("DATA_PATH")

def save_to_file(data, id, date):
    file_name = f"{date}_{id}.json"
    file_path = f'{data_path}data\\{file_name}'
    
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    print(f"JSON 데이터가 {file_path}에 저장되었습니다.")

def save_id_to_txt(id_list):
  if len(id_list) == 0:
    return

  file_name = "id_list.txt"
  file_path = os.path.join(data_path, file_name)

  # 파일이 존재하면 덧붙여 쓰기 위해 'a' 모드를 사용
  with open(file_path, 'a', encoding='utf-8') as txt_file:
      for id_value in id_list:
          txt_file.write(f"{id_value}\n")

# id_completed_list.txt과 가져온 id_list가 겹치는지 확인
def check_completed_id(id_list):
    # 완료 파일 열기
    file_name = 'id_completed_list.txt'
    first_line = ''

    with open(file_name, "r", encoding="utf-8") as file:
      first_line = file.readline().strip()  # 맨 처음 줄을 읽고 공백 제거
    
    if first_line != "":
      id_list_num_arr = list(map(int, id_list))
      first_line_num = int(first_line)
      try:
        id_index = id_list_num_arr.index(first_line_num)
        id_list = id_list[0:id_index]
        return (id_list,True)
      except:
        return (id_list,False)
      
# 기존 id_completed_list.txt에 완료된 id 추가
def add_id_to_completed_id_text_file(id):
  file_name = "id_completed_list.txt"
  file_path = os.path.join(data_path, file_name)

  # 파일이 존재하면 덧붙여 쓰기 위해 'a' 모드를 사용
  with open(file_path, 'a', encoding='utf-8') as txt_file:
      txt_file.write(f"{id}\n")
      
# 기존 id_list.txt 파일 업데이트 -> 기존 텍스트 파일 중 첫 번째 id 삭제
def update_id_list_text_file():
  file_path = "id_list.txt"

  with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

  with open(file_path, "w", encoding="utf-8") as file:
    file.writelines(lines[1:])

# id_list.txt 파일 텍스트 전부 읽기
def get_id_from_id_list_text_file():
  file_path = "id_list.txt"

  with open(file_path, "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file]
  return lines

def save_test_id_to_txt():
  file_name = "id_list_test.txt"
  file_path = os.path.join(f'{data_path}\\data\\', file_name)

  # 파일이 존재하면 덧붙여 쓰기 위해 'a' 모드를 사용
  with open(file_path, 'a', encoding='utf-8') as txt_file:
      for i in range(10918,0,-1):
          txt_file.write(f"{i}\n")