# ----------------------------------------------
# 기능을 가진 모듈 Application
# - Blueprint 인스턴스로 생성
#   - URL : http://127.0.0.1:5000/basic
#   - ~/basic URL 요청 처리해주는 모듈
# ----------------------------------------------
# 모듈로딩 --------------------------------------
from flask import Blueprint, render_template

# BP인스턴스 생성 -------------------------------
bp_basic = Blueprint('basic', 
                     __name__,
                     url_prefix='/basic',
                     template_folder='templates')


# ~/basic URL 요청에 대한 처리 라우팅 -------------
# http://127.0.0.1:5000/basic/
@bp_basic.route('/', endpoint='basic_index')
def basic_index():
    return render_template('basic/index.html')