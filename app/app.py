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

def main():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
