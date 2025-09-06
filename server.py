from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    source = data.get("source", "tr")
    target = data.get("target", "en")

    try:
        response = requests.post(
            "https://libretranslate.de/translate",
            json={
                "q": text,
                "source": source,
                "target": target,
                "format": "text"
            }
        )
        result = response.json()
        return jsonify({"translatedText": result.get("translatedText", "(çeviri yok)")})
    except Exception as e:
        return jsonify({"translatedText": f"(hata: {str(e)})"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
