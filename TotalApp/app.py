# --------------------------------------------------------------
# TotalApp에 대한 초기화 및 설정
# - Flask Web Server 인스턴스 생성
# - 설정 config.py 로딩
# - FWS의 모듈 등록
# - DB 연결 및 초기화
# => 순환참조에 대한 오류 예방 위해 Application Factory로 작성
# --------------------------------------------------------------
# 모듈로딩 ------------------------------------------------------
from flask import Flask, render_template

# ORM Lib 모듈 
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy  

# 전역변수 ------------------------------------------------------
db=SQLAlchemy()
migrate=Migrate()

print('app()')

# 사용자 정의 함수 ----------------------------------------------
# Application Factory 함수 
def create_app():
    print('create_app()')
    
    # FWS 인스턴스 생성
    app = Flask(__name__)
    
    # http://127.0.0.1:5000/ URL에 대한 요청 처리
    # @app.route('/')
    # def index(): return "TotalApp MAIN !!"
    # Application 설정 로딩 -----------------------------
    app.config.from_pyfile('config.py')
    print(f'app.config["DEBUG"] => {app.config["DEBUG"]}')
    print(f'app.config["SQLALCHEMY_DATABASE_URI"] => {app.config["SQLALCHEMY_DATABASE_URI"]}')
    
    # ORM 연동
    from .dbAPP import db_model
     
    db.init_app(app)
    migrate.init_app(app, db)    
       
    
    # 내부 기능 모듈 등록 => 순환참조 예방
    from . import main_view
    from .basicAPP import basic_view
    from .dbAPP import db_view
    app.register_blueprint(main_view.bp_main)
    app.register_blueprint(basic_view.bp_basic)
    app.register_blueprint(db_view.bp_db)
    
    # FWS 인스턴스 반환
    return app