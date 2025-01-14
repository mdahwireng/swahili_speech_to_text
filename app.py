from flask import Flask, render_template, send_from_directory, request
import os   
import pandas as pd
import pickle
import sys
import os
import shutil
import numpy as np
# import pyaudio
from deepspeech import Model
import scipy.io.wavfile as wav
import wave
from werkzeug.utils import secure_filename, send_file

app = Flask(__name__)


MODEL_PATH = 'model/deep.h5'

@app.route("/assets/<path:path>")
def static_dir(path):
    return send_from_directory("static/assets", path)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    global class_names
    if request.method == 'POST':
        print('called')
        # Get the file from post request
        print('Request files', request.files['audio'])
        f = request.files['audio']
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads/audio', secure_filename(f.filename))
        f.save(file_path)
        # print(f)

        #Make Prediction



    







        preds = model_predict(file_path, model)
        shutil.rmtree('./uploads/audio')
        os.mkdir('./uploads/audio')


        return '<h1>Sup World!</h1>'



        # df = pd.read_csv(file_path, parse_dates=True, index_col="Date")
        # # print(df.head())
        # df['Year'] = df.index.year
        # df['Month'] = df.index.month
        # df['Day'] = df.index.day
        # df['WeekOfYear'] = df.index.weekofyear
        # results = make_prediction(df)
        # print('Printing result',results[0])
        # return str(int(results[0]))

@app.route("/about")
def about():
    return "<h1>About</h1>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host="0.0.0", debug=True,port=port)