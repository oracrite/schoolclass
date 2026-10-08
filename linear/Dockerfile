# 1. Base 이미지 선택 (경량화된 slim 버전)
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 바이트코드 생성 방지 및 버퍼링 없는 출력을 위한 환경 변수
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 4. 의존성 파일 복사 및 설치 (캐시 활용을 위해 우선 복사)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. 나머지 소스 코드 복사
COPY . .

# 6. 컨테이너 개방 포트 (예: 8000)
EXPOSE 8000

# 7. 애플리케이션 실행 명령
CMD ["python", "main.py"]
