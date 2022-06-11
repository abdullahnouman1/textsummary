from gc import freeze
import string
from xml.etree.ElementTree import tostring
from flask import Flask, render_template, request, json, redirect, url_for
import flask
from flask_cors import CORS, cross_origin

import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer

app = Flask(__name__)
CORS(app)

@app.route('/summary', methods = [ 'POST'])
def sendSummary(): 
    data = json.loads(request.data)

    parser = PlaintextParser.from_string(data, Tokenizer("english"))
    summarizer = LuhnSummarizer()
    gatherText = summarizer(parser.document, 5)
    summary_list = [str(sentence) for sentence in gatherText]
    summary = ' '.join(summary_list)

    return summary

app.run(debug=True)

#http://127.0.0.1:5000/summary