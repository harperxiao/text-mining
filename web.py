# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:34:28 2018

@author: hp
"""

import time
import flask
from flask import render_template, request, g
import argparse

import compose_poem1 as generate_poem

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'




app = flask.Flask(__name__)

def set_arguments():
    parser = argparse.ArgumentParser(description='Poem Generator')
    parser.add_argument('--host', type=str, default='127.0.0.1',
                        help='host, default is 127.0.0.1.')
    parser.add_argument('--port', type=int, default='5000',
                        help='port, default is 5000.')
    return parser


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentences_count = 4
        poem = ['' for i in range(sentences_count)]
        try:
            poem_1 = request.form['poem_1']
            if poem_1:
                start_words = poem_1
                while True:
                    poem = generate_poem.gen_poem(start_words)
                    print(poem)
                    flag = True
                    if flag:
                        break
        except Exception as e:
            print(e)
        return render_template('index.html',
                                poem_1=poem,
                                )
    return render_template('index.html', g = g)


if __name__ == '__main__':
    parser = set_arguments()
    cmd_args = parser.parse_args()

    print('{} START {}:{}'.format(time.strftime(TIME_FORMAT), cmd_args.host, cmd_args.port))

    app.run(host=cmd_args.host, port=cmd_args.port)

    print('{} STOP'.format(time.strftime(TIME_FORMAT)))









