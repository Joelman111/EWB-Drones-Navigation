from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def main():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
