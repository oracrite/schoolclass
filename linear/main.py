# 필요한 라이브러리 임포트
from flask import Flask, jsonify, request

# Flask 애플리케이션 초기화
app = Flask(__name__)


@app.route("/linear-search", methods=["POST"])
def linear_search():
  """선형 검색 알고리즘을 수행하고 단계별 실행 내역을 반환하는 엔드포인트"""
  try:
    # 클라이언트로부터 JSON 데이터 수신
    data = request.get_json()
    arr = data.get("array", [])
    target = data.get("target")

    steps = []
    found_index = -1

    # 선형 검색 알고리즘 수행 (처음부터 끝까지 순차 탐색)
    for i, val in enumerate(arr):
      is_match = (val == target)

      # 각 단계별 상태 기록 (시각화를 위해 저장)
      steps.append({
          "step": i + 1,
          "index": i,
          "value": val,
          "matched": is_match,
          "message": (
              f"인덱스 [{i}]의 값({val})과 타겟({target})을 비교합니다. -> "
              f"{'일치합니다! (검색 완료)' if is_match else '일치하지 않습니다.'}"
          ),
      })

      if is_match:
        found_index = i
        break  # 값을 찾았으므로 탐색 종료

    # 검색 결과 및 복잡도 정보 반환
    return jsonify({
        "success": True,
        "found_index": found_index,
        "steps": steps,
        "complexity": {
            "time": "O(n) - 최악의 경우 배열 전체를 탐색",
            "space": "O(1) - 추가적인 메모리 공간이 거의 필요 없음",
        },
    })

  except Exception as e:
    return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
  # Cloud Run 환경은 기본적으로 8080 포트를 사용합니다.
  app.run(host="0.0.0.0", port=8080)
