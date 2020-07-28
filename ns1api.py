from flask import Flask, jsonify, request
import requests, json
from ns1 import NS1


app = Flask(__name__)
key = "pbpassw0rd"
api = NS1(apiKey='DwnaRFv3dV6DVRvCmUiP')

@app.route('/external/createa/', methods=['POST']) # External A record creation
def crta():
    req= request.get_json()
    if req['key'] != key:
        return "auth failed", 301

    url = req['url']
    answer = req['answer']
    z = url.split(".")
    z = z[1]
    print(z)
    zone = api.loadZone(z + ".com")
    rec = zone.add_A(url, answer)
    return jsonify(rec.data)
