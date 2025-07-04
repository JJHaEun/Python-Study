# 조선시대 왕 추가하기
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


kings = {
    1: "태조",2:"정종",3:"태종",4:"세종",5:"문종",6:"단종",
    7:"세조",8:"예종",9:"성종",10:"연산군",11:"중종",12:"인종",
    13:"명종",14:"선조",15:"광해군",16:"인조",17:"효종",18:"현종",
    19:"숙종",20:"경종",21:"영조",22:"정조",23:"순조",24:"헌종",
    25:"철종",26:"고종",27:"순종",
}

@app.route("/")
def hello_world():
    return "<p>조선시대 왕 이름 API 서비스</p>"

@app.route("/kings",methods=["GET"])
def get_kings():
    str_kings = {str(k): v for k, v in kings.items()}
    res = make_response(jsonify(str_kings),200)
    return res

@app.route("/kings/<nth>",methods=["POST"])
def add_kings(nth):
    req = request.get_json()
    print(req)
    print(nth)

    kings[nth] = req['name']
    print(kings)

    res = make_response(jsonify({"message":"왕이 생성되었습니다."}),200)
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=True)