from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_path/<coords>')
def get_path(coords):
    #implement
    print(coords)
    return

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


def main():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
