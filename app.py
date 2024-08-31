from flask import Flask, request

app = Flask(__name__)

@app.route('/echo', methods=['GET'])
def echo():
    text = request.args.get('text')
    return f"The given text is: {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)