# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:21:35 2024

@author: USTPC144
"""

from flask import Flask, render_template

app = Flask(__name__)

# トップページ遷移時の処理
@app.route("/index")
def home():
    title = "Sekido Bar"
    body = "home"
    return render_template('index.html', title = title, body = body)

# お店について遷移時の処理
@app.route("/about")
def about():
    title = 'お店について'
    return render_template('about.html', title = title)

# アクセス遷移時の処理
@app.route("/access")
def access():
    title = 'アクセス'
    return render_template('access.html', title = title)

# メニュー遷移時の処理
@app.route("/menu")
def menu():
    title = 'メニュー'
    return render_template('menu.html', title = title)

# お問い合わせ遷移時の処理
@app.route("/contact")
def contact():
    title = 'お問い合わせ'
    return render_template('contact.html', title = title)

#####テスト#####

#####テスト#####

if __name__ == "__main__":
    app.run()