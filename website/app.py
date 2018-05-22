import os
import subprocess
import random
import string

from flask import Flask, request, render_template, url_for, send_file

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
        midi_name = "wb_user.mid"
        midi_fn = get_wb_src_dir() + "Midi/wb_user.mid"
        try:
            request.files[0].save(midi_fn)
        except Exception as e:
            print "Couldn't save midi file, {}".format(e)
            return "<pre>Invalid .midi file</pre>"
    else:
        midi_name = request.form['input-midi']

    # Find the ini file or write the custom ini file
    if request.form['input-ini'] == "Custom":
        try:
            ini_str = ini.get_ini(request.form)
        except Exception as e:
            print "Can't parse parameters, {}".format(e)
            return "<pre>Can't parse the parameters</pre>"
        ini_name = "wb_user.ini"
        ini_fn = get_wb_src_dir() + "Ini/wb_user.ini"
        with open(ini_fn, "w") as f:
            f.write(ini_str)
    else:
        ini_name = request.form['input-ini']


    # Generate the midi 
    ## File names have to be relative to wbClient/src/
    generate_midi(input_midi_fn="Midi/" + midi_name,
                  input_ini_fn="Ini/" + ini_name,
                  output_midi_fn="./output/",
                  single_midi_fn="output.mid")

    single_midi_fn = "output.mid"
    #wav_name = "tmp-{}.wav".format(random_string(6)) # avoid caching
    wav_name = "tmp.wav"
    output_wav_fn = get_app_dir() + "/static/" + wav_name
    convert_midi_to_wav(single_midi_fn, output_wav_fn)

    wav_url = url_for('static', filename=wav_name)
    return render_template('audio.html', wav_url=wav_url)


def convert_midi_to_wav(midi_fn, wav_fn):
    print midi_fn, wav_fn
    command = "timidity {} -Ow -o {}".format(midi_fn, wav_fn)
    try:
        process = subprocess.Popen(command, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        print stdout, stderr
    except Exception as e:
        print "Couldn't convert midi, {}".format(e)
        raise e


def generate_midi(input_midi_fn="Midi/mary.mid",
                  input_ini_fn="Ini/Space.ini",
                  output_midi_fn="./output/",
                  single_midi_fn="output.mid"):
    print input_ini_fn, input_midi_fn, output_midi_fn
    generate_midi_files_command = ("./generate_melody.sh -m " +
                                   input_midi_fn +
                                   " -i " + input_ini_fn + " -o " +
                                   output_midi_fn)
    print generate_midi_files_command

    combine_midi_files_command = ("./combine_midi.sh " + output_midi_fn +
                                  " " + single_midi_fn)
    # command = ["./generate_melody.sh"]
    try:
        print subprocess.Popen(generate_midi_files_command,
                               shell=True,
                               stdout=subprocess.PIPE).stdout.read()
        print subprocess.Popen(combine_midi_files_command,
                               shell=True,
                               stdout=subprocess.PIPE).stdout.read()
        # output = subprocess.check_output(command)
    except Exception as e:
        print "Couldn't generate midi, {}".format(e)
        raise e


def get_app_dir():
    return os.path.dirname(os.path.realpath(__file__))

def get_wb_src_dir():
    return (get_app_dir()[:-7] + 'watson-beat/src/')

def random_string(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits)
                   for _ in range(N))
