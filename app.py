# -*- coding: utf-8 -*-
from random import shuffle
import sys, os, codecs

from flask import Flask, render_template, redirect, url_for, session, request
from werkzeug import secure_filename

# Mitigation for this error: UnicodeDecodeError: 
# 'ascii' codec can't decode byte 0xe2 in position 13: ordinal not in range(128)
reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

app = Flask(__name__, static_folder="static", static_url_path='/static')

with open("static/english-1.txt") as f:
	lines = f.readlines()
	shuffle(lines)
	for line in lines:
		line.decode('utf-8')
		question, rightAnswer = line.strip().split("\t")


@app.route('/', methods=["GET", "POST"])
def index():
	return render_template('index.html', lines=lines, question=question, rightAnswer=rightAnswer)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
