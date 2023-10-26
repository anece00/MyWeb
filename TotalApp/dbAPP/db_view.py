# ----------------------------------------------
# 기능을 가진 모듈 Application
# - Blueprint 인스턴스로 생성
#   - URL : http://127.0.0.1:5000/db
#   - ~/db URL 요청 처리해주는 모듈
# ----------------------------------------------
# 모듈로딩 ---------------------------------------------------
from flask import Blueprint, render_template
from flask import request, url_for, redirect

# DB관련 요청 처리 위한 모듈
from TotalApp.dbAPP.db_model import User
from TotalApp.app import db
from datetime import datetime

# BP인스턴스 생성 ----------------------------------------------
bp_db = Blueprint('a', 
                     __name__,
                     url_prefix='/db',
                     template_folder='templates')

# ~/db URL 요청에 대한 처리 라우팅 ------------------------------
# http://127.0.0.1:5000/db 
# http://127.0.0.1:5000/db/
@bp_db.route('/')
def db_index():
    return render_template('db/index.html')

# 사용자 등록 요청 처리 ------------------------------------
# http://127.0.0.1:5000/db/user_reg
@bp_db.route('/user_reg')
def user_reg():
    print("DDDDD ====> user_reg()")
    return render_template('db/user_reg.html')

# 현재 사용자 목록 요청 처리 -------------------------------
# http://127.0.0.1:5000/db/user_list
@bp_db.route('/user_list/')
def user_list():
    # DB에 등록된 회원조회 데이터 전달 
    users=User.query.order_by(User.created_at.desc())
    print(f' users : {users}')
    # HTML 내부에 user_list변수 사용
    return render_template('db/user_list.html', user_list=users)

# DB에 사용자 추가 요청 처리 ----------------------------------
# URL => http://127.0.0.1:5000/db/user_insert
@bp_db.route('/user_insert', methods=['POST'])
def user_insert():
    # request 객체에서 데이터만 추출 
    #id_=request.form['id']  # auto_increment로 자동 증가
    username_ = request.form['username']
    email_ = request.form['email']
    
    # Table에 새로운 user 저장
    user_ = User(username=username_, 
                 email=email_, 
                 created_at=datetime.now())
    db.session.add(user_)  
    db.session.commit()     # 실제 DB에 반영
   
    print( "INSERT OK" )
    # url_for(endpoint)
    return redirect(url_for('a.user_list'))






# @bp_db.route('/list/')
# def _list():
#     question_list = Question.query.order_by(Question.create_date.desc())
#     return render_template('db/question_list.html', question_list=question_list)


# @bp_db.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)
#     return render_template('question/question_detail.html', question=question) 


# @bp_db.route('/insert/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)
#     return render_template('question/question_detail.html', question=question) 