from flask import Flask, request
app = Flask(__name__)

@app.route("/trigger", methods=["POST"])
def trigger():
    print("📣 ALERT RECEIVED:", request.json)
    return "OK"

app.run(port=4000)
