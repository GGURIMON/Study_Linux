# 정규식 표현을 지원하는 라이브러리
import re

# 파일 목록이 저장된 파일 경로
file_path = "logs2"

# 이미지 파일을 추출하기 위한 정규 표현식
# compile로 추출이며 r은 정규식임을 나타냄
pattern = re.compile(r'(\w+)\(([\w\.]+):(\d+)\)')

# 파일을 열어 각 줄에 대해 정규 표현식을 적용
# open만 사용하면 close를 작성하여 메모리 소모를 하지않게 해야하지만
# with를 같이 사용하면 작동 후 자동으로 닫힘
with open(file_path, 'r') as file:
    for line in file:
        file_name = line.strip() # 줄 끝의 개행 문자 제거
        match = pattern.search(file_name) # 파일 이름이 위 패턴에 맞는 것을 추출
        if match: # 만일 매치한다면
            print(f"메소드명: {match.group(1)}, 파일이름: {match.group(2)}, \
                  \n 줄번호: {match.group(3)}") # 출력