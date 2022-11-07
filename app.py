import hashlib

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import config

app = Flask(__name__)

#db
client = MongoClient('mongodb+srv://imjoo0:wndud234@cluster0.cllvh7u.mongodb.net/?retryWrites=true&w=majority')
db = client.dbLMS

# doc = {
#     'id':2,
#     'user_category_name':'학생'
# }
# db.user_category.insert_one(doc)
# @app.route('/')
# def home():
    # return check_token('main.html')

# 로그인 API
# @app.route("/api/login", methods=['POST'])
# def login_proc():
#     user_id = request.form['id_give']
#     password = request.form['pw_give']
#     hashed_pw = hashlib.sha256(password.encode('utf-8')).hexdigest()
#
#     user = db.users.find_one({'user_id': user_id, 'password': hashed_pw})
#
#     if user is not None:
#         payload = {'id': user_id,
#                    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=1800)}
#
#         return jsonify({
#             'result': 'success',
#             # 검증된 경우, access 토큰 반환
#             'token': jwt.encode(payload, SECRET_KEY, algorithm='HS256')
#         })
#     else:
#         return jsonify({'result': 'fail', 'msg': '아이디 또는 비밀번호가 일치하지 않습니다.'})
#
#
# # 로그아웃 API
# @app.route("/api/logout", methods=['GET'])
# def logout_proc():
#     token_receive = request.cookies.get('token')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         return jsonify({
#             'result': 'success',
#             'token': jwt.encode(payload, SECRET_KEY, algorithm='HS256'),
#             'msg': '로그아웃 성공'
#         })
#     except jwt.ExpiredSignatureError or jwt.exceptions.DecodeError:
#         return jsonify({
#             'result': 'fail',
#             'msg': '로그아웃 실패'
#         })
#
# @app.route('/perform')
# def perform():
#    return render_template('perform.html')
#
# @app.route('/user')
# def student():
#    return render_template('user.html')
#
# if __name__ == '__main__':
#    app.run('0.0.0.0',port=6725,debug=True)
#
# @app.route('/test',methods = ['GET'])
# def test_get():
#     title_receive = request.args.get('title_give')
#     print(title_receive)
#     return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})

@app.route('/perform')
def perform():
   return render_template('perform.html')

@app.route('/user')
def student():
   return render_template('user.html')

if __name__ == '__main__':
   app.run('0.0.0.0',port=6725,debug=True)