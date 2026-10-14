from flask import Flask

# 'app'이라는 이름으로 플라스크 객체를 만듭니다. (gunicorn이 이걸 찾습니다!)
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Cloud Run! 배포 성공!"

if __name__ == "__main__":
    import os
    # 혹시 모를 로컬 테스트용 코드
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
