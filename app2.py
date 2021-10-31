from flask import Flask, request, send_file, render_template, redirect, jsonify, Response
from flask import send_from_directory, abort
from werkzeug.utils import secure_filename
from deep_translator import GoogleTranslator
# from werkzeug import secure_filename
import os
import json
import pandas as pd
import numpy as np
import regex as re
import csv


with open('config.json', 'r') as c:
    location = json.load(c)["location"]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = location['upload_location']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods = ['POST'])  
def success():  
    # global output_file
    global M
    if request.method == 'POST':  
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))) 
        # json_file=f.filename
        # output_file=format(json_file)
        # f.save(f.filename)  
        M = f.filename
        # output_file.save(output_file)  
        return render_template("success.html", name = f.filename) 
        
@app.route('/download')
def download_file():
    # output=output_file
    return send_file(M, as_attachment = True)
    # return 'hello google app engine!'

@app.route('/view')
def view_file():
    # p= M
#     data_file = open('D:\flask\output_file.csv', 'w', newline='')
# csv_writer = csv.writer(data_file)



    return send_file(M, file_name= "xyz.json", as_attachment = True)


if (__name__=="__main__"):
    app.run(debug=True, port=5000)