from flask import Flask
app = Flask(__name__)

@app.route('/<resource>/now', methods=['GET'])
def get_stats(resource):
    return

