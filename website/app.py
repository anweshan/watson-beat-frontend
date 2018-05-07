from flask import Flask, request, render_template

from util import ini

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    s = ini.get_ini(request.form)
    return "<pre>{}</pre>".format(s)
#    try:
#        s = ini.get_ini(request.form)
#        return '<pre>{}</pre>'.format(s)
#    except Exception as e:
#        print "Failed to write ini, error: {}".format(e)
#        raise e
#    return ''.join('<p>{}: {}</p>'.format(key, val)
#                   for key, val in sorted(request.form.iteritems()))
