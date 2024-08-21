import re

file_path = 'logs2'

pattern = re.compile(r'(E/\(\s\d+\)):\s+([\w\s]+\.\w+)\.(\w+)\(([\w\.]+):(\d+)\)')

with open(file_path, 'r') as file:
    for line in file:
        file_name = line.strip()
        match = pattern.match(file_name)
        if match:
            print(f"에러 코드 = {match.group(1)} 에러 위치 = {match.group(2)} 파일명.파일확장자:줄번호 = {match.group(3)}({match.group(4)}.{match.group(5)})")
            