from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    print request.form.keys()
    return ', '.join('{}: {}'.format(key, val)
                     for key, val in request.form.iteritems())
