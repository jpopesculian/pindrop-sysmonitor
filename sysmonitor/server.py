from flask import Flask, jsonify, request
from .repo import fetch, fetch_last, connect

app = Flask(__name__)
# app.debug = True

@app.route('/api/v1/<resource>', methods=['GET'])
def get_stat_list(resource):
    conn = connect()
    filters = dict()
    for arg_name in ['sort', 'page', 'size']:
        try:
            arg = int(request.args.get(arg_name))
        except (ValueError, TypeError):
            continue
        filters[arg_name] = arg
    result = fetch(conn, str.capitalize(resource), **filters)
    return jsonify(**result)

@app.route('/api/v1/<resource>/last', methods=['GET'])
def get_stats(resource):
    conn = connect()
    result = fetch_last(conn, str.capitalize(resource))
    return jsonify(**result)

