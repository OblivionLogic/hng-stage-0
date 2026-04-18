import requests
from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_info():
    # Fetch random cat fact
    try:
        fact_response = requests.get("https://catfact.ninja/fact")
        cat_fact = fact_response.json().get('fact', 'No fact found')
    except:
        cat_fact = "Could not fetch cat fact"

    return jsonify({
        "email": "dicekhandy@gmail.com",
        "current_datetime": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "github_url": "https://github.com",
        "fact": cat_fact
    }), 200

if __name__ == '__main__':
    app.run()
