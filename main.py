from flask import Flask, render_template, request
import logging

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    logging.info(request.host)
    return render_template('top.html')

@app.route('/frame/<counter>', methods=['GET'])
def frame(counter):
    logging.info(request.host)
    return render_template('frame.html', counter=counter)

if __name__ == "__main__":
    app.run(debug=True)