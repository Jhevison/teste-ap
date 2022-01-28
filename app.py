from flask import Flask

app = Flask(__name__)
@app.route('/', methods=['GET'])
def respond():
    return {"ola": "Mundo"}


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
