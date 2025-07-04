from flask import Flask, render_template, request, jsonify, make_response
from googletrans import Translator
import asyncio

app = Flask(__name__)
simpago = Translator()

@app.route("/")
def index():
    return render_template('index.html')



@app.route("/translate", methods=["POST"])
def translate():
    req = request.get_json()
    trans_src = req["trans_src"]

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # 코루틴 처리
    trans_dest = loop.run_until_complete(simpago.translate(trans_src, dest="en", src="ko"))

    print(trans_dest.text)

    res = make_response(jsonify({"result": trans_dest.text}), 200)
    return res





if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001, debug=True)