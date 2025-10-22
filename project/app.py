from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def start():
    return render_template("index.html")

if __name__ == '_main_':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)