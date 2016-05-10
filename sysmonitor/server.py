from flask import Flask, jsonify
from .repo import fetch, fetch_last, connect

app = Flask(__name__)
app.debug = True

@app.route('api/v1/<resource>', methods=['GET'])
def get_stat_list(resource):
    conn = connect()
    result = fetch(conn, str.capitalize(resource))
    return jsonify(**result)

@app.route('api/v1/<resource>/last', methods=['GET'])
def get_stats(resource):
    conn = connect()
    result = fetch_last(conn, str.capitalize(resource))
    return jsonify(**result)

