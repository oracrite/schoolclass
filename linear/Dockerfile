# 파이썬 공식 이미지를 사용합니다
FROM python:3.9-slim

# 작업 폴더를 지정합니다
WORKDIR /app

# 필요한 패키지 목록 파일을 복사하고 설치합니다
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드를 전부 복사합니다
COPY . .

# 컨테이너가 실행될 때 웹 서버를 띄우는 명령어를 입력합니다 (예: main.py 실행)
CMD ["python", "main.py"]
