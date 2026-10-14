# 파이썬 공식 이미지 사용
FROM python:3.9-slim

# 작업 폴더를 linear 안으로 지정합니다.
WORKDIR /app

# 현재 linear 폴더 안에 있는 모든 파일을 컨테이너 안으로 복사합니다.
COPY . /app

# 필요한 패키지를 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt

# 클라우드 런이 지정해주는 PORT 환경변수를 사용하여 서버를 실행합니다.
# (만약 파일 이름이 main.py가 아니라면 아래 명령어의 main.py를 알맞게 수정해주세요!)
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app
