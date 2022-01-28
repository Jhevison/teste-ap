from flask import Flask, jsonify
import choose

app = Flask(__name__)
@app.route('/', methods=['GET'])
def respond():
    quote = choose.returnQuote()
    dict = {}
    dict['quote'] = quote
    return jsonify(dict)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
