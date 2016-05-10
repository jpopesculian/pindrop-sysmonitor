from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_stats():
    return 'Hello World'

