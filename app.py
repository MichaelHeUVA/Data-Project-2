from flask import Flask, request, jsonify
from gemini import get_gemini_response

app = Flask(__name__)


@app.route("/ask", methods=["GET"])
def ask():
    question = request.args.get("question")
    if question:
        print(question)
        return jsonify(
            {
                "response": get_gemini_response(question),
            }
        ), 200
    else:
        return jsonify(
            {"error": "No question provided. Use /ask?question=your question here"}
        ), 400


if __name__ == "__main__":
    app.run(port=5001)
