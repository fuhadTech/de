from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Hello from your Python app on Koyeb!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
