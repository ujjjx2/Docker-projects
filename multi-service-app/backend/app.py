from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(
        {
            'message': 'Hello from backend API',
            'timestamp': datetime.datetime.now().strftime("%F %H:%M:%S"),
            'hostname': socket.gethostname(),
            'version': '1.0.0'
        }
    )
@app.route('/health')
def health():
    return jsonify(
        {
            'result': 'OK - healthy'
        }
    ), 200  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
