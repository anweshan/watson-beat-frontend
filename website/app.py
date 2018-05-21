import os
import subprocess

from flask import Flask, request, render_template, url_for

from util import ini

wb_home="../watson-beat/src"
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Find the midi file or write the custom midi file
    if request.form['input-midi'] == "Custom":

        midi_fn = "/tmp/wb_user.mid"
        try:
            request.files[0].save(midi_fn)
        except Exception as e:
            print "Couldn't save midi file, {}".format(e)
            return "<pre>Invalid .midi file</pre>"
    else:
        midi_fn = "../wbClient/src/Midi/" + request.form['input-midi']

    # Find the ini file or write the custom ini file
    if request.form['input-ini'] == "Custom":
        try:
            ini_str = ini.get_ini(request.form)
        except Exception as e:
            print "Can't parse parameters, {}".format(e)
            return "<pre>Can't parse the parameters</pre>"
        ini_fn = "/tmp/wb_user.ini"
        with open(ini_fn, "w") as f:
            f.write(ini_str)
    else:
        ini_fn = "../wbClient/src/Ini/" + request.form['input-ini']

    output_midi_fn = get_app_dir()[:-7] + "/wbClient/src/Midi/ode_to_joy.mid"
    output_wav_fn = get_app_dir() + "/static/tmp.wav"
    convert_midi_to_wav(output_midi_fn, output_wav_fn)

    return render_template('audio.html', wav_fn="tmp.wav")


def convert_midi_to_wav(midi_fn, wav_fn):
    print midi_fn, wav_fn
    command = ["timidity", midi_fn, "-Ow", "-o", wav_fn]
    try:
        output = subprocess.check_output(command) 
    except Exception as e:
        print "Couldn't convert midi, {}".format(e)
        raise e


def generate_midi(input_midi_fn="Midi/mary.mid", input_ini_fn="Ini/Space.ini", output_midi_fn="./output/"):
    print input_ini_fn, input_midi_fn, output_midi_fn
    command = "./generate_melody.sh -m " + input_midi_fn + " -i " + input_ini_fn + " -o " + output_midi_fn
    print command
    # command = ["./generate_melody.sh"]
    try:
        print subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()
        # output = subprocess.check_output(command)
    except Exception as e:
        print "Couldn't generate midi, {}".format(e)
        raise e


def get_app_dir():
    return os.path.dirname(os.path.realpath(__file__))
