# ----------------------------------------------
# 기능을 가진 모듈 Application
# - Blueprint 인스턴스로 생성
# - 데이터베이스의 테이블을 클래스로 정의
# - DB관련 클래스, 함수, 메서드 제어
# ----------------------------------------------
from TotalApp.app import db
from datetime import datetime

# User Table과 맴핑될 Class
class User(db.Model):
    # Table의 컬럼 정의하는 클래스 변수
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), index=True)
    email = db.Column(db.String(100), unique=True, index=True)
    #password_hash=db.Column(db.String)
    created_at =db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)



# class Question(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     subject = db.Column(db.String(200), nullable=False)
#     content = db.Column(db.Text(), nullable=False)
#     create_date = db.Column(db.DateTime(), nullable=False)

# class Answer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
#     question = db.relationship('Question', backref=db.backref('answer_set'))
#     #question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
#     content = db.Column(db.Text(), nullable=False)
#     create_date = db.Column(db.DateTime(), nullable=False)