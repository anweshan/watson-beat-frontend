from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    return ''.join('<p>{}: {}</p>'.format(key, val)
                   for key, val in sorted(request.form.iteritems()))
