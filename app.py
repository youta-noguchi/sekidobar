# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:21:35 2024

@author: USTPC144
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/access")
def access():
    return render_template('access.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

#####テスト#####

#####テスト#####

if __name__ == "__main__":
    app.run()