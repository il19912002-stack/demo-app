import os
from flask import Flask

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "unknown")

def add(a, b):
 return a + b
def divide(a, b):
 if b == 0:
 raise ValueError("Деление на ноль недопустимо")
 return a / b

@app.route("/")
def index():
 return f"demo-app версии{APP_VERSION}, узел{os.uname().
nodename}\n"

@app.route("/health")
 health():
 return {"status": "ok", "version": APP_VERSION}, 200

if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host="0.0.0.0", port=port)
