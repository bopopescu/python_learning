# -*- encoding: utf-8 -*-
"""
@File : main
@Time : 2020/5/18 0:02
@Author : lryself
@Version : 1.0
@Contact : lnolvwe@163.com
"""
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app
# here put the import lib

@app.route('/')
@app.route('/index')
# @login_required
def index():
    # posts = [
    #     {
    #         'author': {'username': 'John'},
    #         'body': 'Beautiful day in Portland!'
    #     },
    #     {
    #         'author': {'username': 'Susan'},
    #         'body': 'The Avengers movie was so cool!'
    #     }
    # ]
    # return render_template('index.html', title='Home', posts=posts)
    return "Hello, World!"