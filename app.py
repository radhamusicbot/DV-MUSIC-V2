import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Radhe Radhe"

if __name__ == "__main__":
    # Port number dynamically set karne ke liye os.getenv ka use karte hain
    port = int(os.getenv("PORT", 8000))  # Default port 8000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
