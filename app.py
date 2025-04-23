from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
classifier = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        text = request.form["text"]
        result = classifier(text)[0]
        sentiment = {
            "label": result["label"],
            "score": round(result["score"] * 100, 2)
        }
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
