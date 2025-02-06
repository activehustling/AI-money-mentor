from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['GET'])
def ask():
    question = request.args.get('question', '').lower()

    # Simple AI response logic
    answers = {
        "how can i earn money online?": "You can try freelancing, affiliate marketing, or blogging.",
        "what is the best passive income?": "Investing in stocks, real estate, or digital products.",
        "how to start freelancing?": "Sign up on Fiverr or Upwork and offer your skills."
    }

    response = answers.get(question, "I don't know the answer yet, but keep learning!")

    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
