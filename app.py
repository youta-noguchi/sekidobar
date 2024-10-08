# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 10:21:35 2024

@author: USTPC144
"""

from flask import Flask, render_template, request
from flask_mail import Mail, Message
# import pdb

app = Flask(__name__)

#メール設定
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587                             # TLSは587、SSLなら465
app.config['MAIL_USERNAME'] = 'yekoutesutoyong759@gmail.com'
app.config['MAIL_PASSWORD'] = 'hoddmrgroedcndfm'        # GmailのApp用のmパスワード設定をしておく必要あり
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'yekoutesutoyong759@gmail.com'    # これがあるとsender設定が不要になる
mail = Mail(app)

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
@app.route("/contact", methods=['GET'])
def contact():
    title = 'お問い合わせ'
    return render_template('contact.html', title = title)

# お問い合わせ送信時の処理
@app.route("/contact", methods=['POST'] )
def send_email():

#   Form内容受取
    username    = request.form['data1'].strip()
    hurigana    = request.form['data2'].strip()
    email       = request.form['data3'].strip()
    description = request.form['data4'].strip()

#   入力値チェック
    if username == '' or hurigana == '' or email == '' or description == '':
        errflg = 'X'
        title = 'お問い合わせ'
        return render_template('contact.html', title = title, errflg = errflg)
    else:
#       メール作成
        msg = Message('SekidoBarホームページ　お問い合わせ', recipients=['noguchi@ust-solution.co.jp'])
        msg.body = f"お名前：{username}\nふりがな：{hurigana}\nメールアドレス：{email}\n問い合わせ内容：\n{description}"
        mail.send(msg)
    
    title = 'お問い合わせ完了'
    return render_template('contact.html', title = title)

if __name__ == "__main__":
    app.run()