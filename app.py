from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_info():
    return jsonify({
        "email": "dicekhandy@gmail.com",
        "current_datetime": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "github_url": "https://github.com"
    }), 200

if __name__ == '__main__':
    app.run()
