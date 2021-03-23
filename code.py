from flask import Flask
from datetime import date
import os
from flask import jsonify


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def motd(path):
    t = str(date.today())
    return jsonify({'message': "Hello its:"+t})

if __name__ == '__main__':
    static_port = 8080
    dynamic_port = os.environ.get('PORT')
    if dynamic_port != None:
        static_port = dynamic_port
    app.run(host='0.0.0.0', port=static_port)
