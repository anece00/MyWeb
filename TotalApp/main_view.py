# ----------------------------------------------
# 기능을 가진 모듈 Application
# - Blueprint 인스턴스로 생성
#   - URL : http://127.0.0.1:5000/basic
#   - ~/basic URL 요청 처리해주는 모듈
# ----------------------------------------------
# 모듈로딩 --------------------------------------
from flask import Blueprint, render_template, url_for, redirect
from .dbAPP import db_view
from .basicAPP import basic_view

# BP인스턴스 생성 -------------------------------
bp_main = Blueprint('/', 
                     __name__,
                     template_folder='templates')


# ~/basic URL 요청에 대한 처리 라우팅 -------------
# http://127.0.0.1:5000/
@bp_main.route('/')
def main_index():
    return render_template('main/index.html')

# # http://127.0.0.1:5000/go_basic
# @bp_main.route('/.go_basic')
# def go_basic():
#     print(f' url_for("basic_index") : {url_for("basic.basic_index")}')
#     return f"BASIC BASIC BASIC : { url_for('basic_index') }"
# return  redirect( url_for('db.db_index') )

# # http://127.0.0.1:5000/.go_db
# @bp_main.route('/.go_db')
# def go_db():
#     print(f' url_for("db_index") : {url_for("db.db_index")}')
#     return  redirect( url_for('db.db_index') )