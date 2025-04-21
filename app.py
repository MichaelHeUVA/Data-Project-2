from flask import Flask, request, jsonify
from gemini import get_gemini_response

app = Flask(__name__)


@app.route("/ask", methods=["GET"])
def ask():
    question = request.args.get("question")
    try:
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
    except Exception as e:
        print(f"Error: {e}")
        return jsonify(
            {"error": "An error occurred while processing your request."}
        ), 500


if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0")
